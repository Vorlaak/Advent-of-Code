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
    start = 50
    for op in op_list:
        start += op
        start %= 100
        if start == 0:
            counter += 1
    print(counter)


if __name__ == "__main__":
    main()
