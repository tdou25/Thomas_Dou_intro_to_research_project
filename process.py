def trim_main():
    file1 = open("train.csv", "r")
    file2 = open("test.csv", "r")
    
    fileOut = open("noIrony.csv","w")

    trainFileLines = file1.readlines()
    testFileLines = file2.readlines()

    #
    for line in trainFileLines:
        words = line.split(",")
        print(words[-1])
        if words[-1] == "sarcasm\n" or words[-1] == "regular\n" or words[-1] == "figurative\n":
            print(line)
            print("\n")
            fileOut.write(line)

    for line in testFileLines:
        words = line.split(",")
        print(words[-1])
        if words[-1] == "sarcasm\n" or words[-1] == "regular\n" or words[-1] == "figurative\n":
            print(line)
            print("\n")
            fileOut.write(line)


def trim_make_two():
    file1 = open("train.csv", "r")
    file2 = open("test.csv", "r")
    
    fileTrain = open("trainNoIrony.csv","w")
    fileTest = open("testNoIrony.csv","w")

    trainFileLines = file1.readlines()
    testFileLines = file2.readlines()

    #
    for line in trainFileLines:
        words = line.split(",")
        print(words[-1])
        if words[-1] == "sarcasm\n" or words[-1] == "regular\n" or words[-1] == "figurative\n":
            print(line)
            print("\n")
            fileTrain.write(line)

    for line in testFileLines:
        words = line.split(",")
        print(words[-1])
        if words[-1] == "sarcasm\n" or words[-1] == "regular\n" or words[-1] == "figurative\n":
            print(line)
            print("\n")
            fileTest.write(line)

def make_tiny():
    with open("noIrony.csv", "r") as file1, open("tinySet.csv", "w") as fileOut:
        lines = file1.readlines()

        srcsmcnt = 0
        figcnt = 0
        regcnt = 0

        for line in lines:
            words = line.split(",")
            label = words[-1].strip()  # Remove newline character

            if label == "sarcasm" and srcsmcnt >= 400:
                continue
            if label == "figurative" and figcnt >= 400:
                continue
            if label == "regular" and regcnt >= 400:
                continue

            if label in ["sarcasm", "regular", "figurative"]:
                fileOut.write(line)

                if label == "sarcasm":
                    srcsmcnt += 1
                elif label == "figurative":
                    figcnt += 1
                elif label == "regular":
                    regcnt += 1

if __name__ == "__main__":
    #trim_main()
    trim_make_two()
    make_tiny()
    pass
