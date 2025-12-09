def get_input():
    # return "example.txt"
    return "input.txt"


def get_lists(text, op_list):
    with open(text) as file:
        for line in file:
            match line[0]:
                case "L":
                    op_list.append(-1 * int(line[1:]))
                case "R":
                    op_list.append(int(line[1:]))


def main():
    textfile = get_input()
    op_list = []
    get_lists(textfile, op_list=op_list)
    counter = 0
    pointer = 50
    was_zero = False
    for op in op_list:
        changing = 0
        was_zero = False
        if pointer == 0:
            changing -= 1
        pointer += op
        if pointer == 0:
            counter += 1
            was_zero = True
        while pointer < 0:
            pointer += 100
            changing += 1
        if pointer == 0 and not was_zero:
            counter += 1
        while pointer >= 100:
            pointer -= 100
            counter += 1
        counter += max(0, changing)


if __name__ == "__main__":
    main()
