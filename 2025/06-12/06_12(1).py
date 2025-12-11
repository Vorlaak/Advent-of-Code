def get_input():
    # return "example.txt"
    return "input.txt"


def get_operations(text):
    with open(text) as file:
        data = file.read().split("\n")[:-1]
    operations = []
    for el in data[0].split(" "):
        if el != "":
            operations.append([el])
    for i in range(1, len(data)):
        new_line = data[i].split(" ")
        counter = 0
        for j in range(len(new_line)):
            if new_line[j] != "":
                operations[counter].append(new_line[j])
                counter += 1
    return operations


def process_operation(operation):
    counter = 0
    if operation[-1] == "*":
        counter = 1
        for i in range(len(operation) - 1):
            counter *= int(operation[i])
    elif operation[-1] == "+":
        counter = 0
        for i in range(len(operation) - 1):
            counter += int(operation[i])
    return counter


def main():
    textfile = get_input()
    operations = get_operations(textfile)
    counter = 0
    for op in operations:
        counter += process_operation(op)
    print(counter)


if __name__ == "__main__":
    main()
