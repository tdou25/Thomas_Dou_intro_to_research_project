from datasets import Dataset
import pandas as pd
from transformers import BertTokenizer, BertForSequenceClassification, Trainer, TrainingArguments
import torch
from sklearn.preprocessing import LabelEncoder

def tokenize_function(examples):
    return tokenizer(examples['text'], padding="max_length", truncation=True)

def custom_data_collator(features):
    batch = {}
    for key in features[0].keys():
        if key == "labels":
            batch[key] = torch.tensor([f[key] for f in features], dtype=torch.long).to(device)
        else:
            batch[key] = torch.stack([torch.tensor(f[key], dtype=torch.long) for f in features]).to(device)
    return batch

if __name__ == "__main__":
    # Assuming you have your data in a CSV file
    df = pd.read_csv('tinySet.csv')

    # Encode the categorical labels into integers
    label_encoder = LabelEncoder()
    df['label'] = label_encoder.fit_transform(df['label'])

    # Convert the DataFrame to a Hugging Face Dataset
    dataset = Dataset.from_pandas(df)

    # Split the dataset into train and test sets
    dataset = dataset.train_test_split(test_size=0.2)

    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

    tokenized_datasets = dataset.map(tokenize_function, batched=True)

    tokenized_datasets = tokenized_datasets.remove_columns(['text'])
    tokenized_datasets = tokenized_datasets.rename_column('label', 'labels')
    tokenized_datasets.set_format('torch')

    device = torch.device("mps") if torch.backends.mps.is_available() else torch.device("cpu")

    # Move model to device
    model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=len(label_encoder.classes_)).to(device)

    training_args = TrainingArguments(
        output_dir='./results',          # output directory
        num_train_epochs=3,              # number of training epochs
        per_device_train_batch_size=8,   # batch size for training
        per_device_eval_batch_size=8,    # batch size for evaluation
        warmup_steps=500,                # number of warmup steps for learning rate scheduler
        weight_decay=0.01,               # strength of weight decay
        logging_dir='./logs',            # directory for storing logs
        logging_steps=10,
    )

    trainer = Trainer(
        model=model,                         # the instantiated 🤗 Transformers model to be trained
        args=training_args,                  # training arguments, defined above
        train_dataset=tokenized_datasets['train'],         # training dataset
        eval_dataset=tokenized_datasets['test'],           # evaluation dataset
        data_collator=custom_data_collator,               # using custom data collator
    )

    trainer.train()
    results = trainer.evaluate()
    print(results)
    model.save_pretrained('./sarcasm_figurative_regular_model')
    tokenizer.save_pretrained('./sarcasm_figurative_regular_model')

    from transformers import pipeline

    classifier = pipeline('text-classification', model='./sarcasm_figurative_regular_model', tokenizer=tokenizer, device=0 if torch.backends.mps.is_available() else -1)

    new_tweets = ["I just love waiting in traffic for hours.", "The sun is shining bright today!", "His words cut deeper than a knife."]
    predictions = classifier(new_tweets)
    print(predictions)
