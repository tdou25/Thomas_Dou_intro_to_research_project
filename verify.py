if __name__ == "__main__":
    with open("test_prompt_output.csv", "r") as file:
        lines = file.readlines()

    total_correct = 0

    # False negative types (expected_to_actual)
    sar_to_fig = 0
    sar_to_reg = 0

    fig_to_sar = 0
    fig_to_reg = 0

    reg_to_sar = 0
    reg_to_fig = 0

    for line in lines:
        pair = line.strip().split(",")
        expected = pair[0].strip()
        actual = pair[1].strip()

        if expected not in ["sarcasm", "figurative", "regular"]:
            continue

        print(expected + ",")
        print(actual + "\n")

        if actual == expected:
            total_correct += 1
        elif expected == "sarcasm":
            if actual == "figurative":
                sar_to_fig += 1
            elif actual == "regular":
                sar_to_reg += 1
        elif expected == "figurative":
            if actual == "sarcasm":
                fig_to_sar += 1
            elif actual == "regular":
                fig_to_reg += 1
        elif expected == "regular":
            if actual == "sarcasm":
                reg_to_sar += 1
            elif actual == "figurative":
                reg_to_fig += 1

    message = f"TOTAL CORRECT: {total_correct}\n\n"
    message += "FALSE NEGATIVES (expected -> actual):\n"
    message += f"sarcasm -> figurative: {sar_to_fig}\n"
    message += f"sarcasm -> regular: {sar_to_reg}\n"
    message += f"figurative -> sarcasm: {fig_to_sar}\n"
    message += f"figurative -> regular: {fig_to_reg}\n"
    message += f"regular -> sarcasm: {reg_to_sar}\n"
    message += f"regular -> figurative: {reg_to_fig}\n"

    print(message)
