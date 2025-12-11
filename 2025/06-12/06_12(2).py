def get_input():
    # return "example.txt"
    return "input.txt"


def get_operations(text):
    with open(text) as file:
        data = file.read().split("\n")[:-1]
    limits = []
    for i, el in enumerate(data[-1]):
        if i != 0 and el != " ":
            limits.append(i - 1)
    limits.append(len(data[-1]) - 1)
    return data, limits


def process_operation(data, previous_limit, limit):
    counter = 0
    numbers = []
    for j in range(previous_limit, limit + 1):
        numbers.append([data[0][j]])
    for i in range(1, len(data) - 1):
        for j in range(previous_limit, limit + 1):
            numbers[j - previous_limit].append(data[i][j][0])
    if data[-1][previous_limit] == "*":
        counter = 1
        for number in numbers:
            num = 0
            for el in number:
                if el != " ":
                    num *= 10
                    num += int(el)
            if num != 0:
                counter *= num

    elif data[-1][previous_limit] == "+":
        counter = 0
        for number in numbers:
            num = 0
            for el in number:
                if el != " ":
                    num *= 10
                    num += int(el)
            counter += num
    return counter


def main():
    textfile = get_input()
    data, limits = get_operations(textfile)
    counter = 0
    previous_limit = 0
    for limit in limits:
        counter += process_operation(data, previous_limit, limit)
        previous_limit = limit + 1
    print(counter)


if __name__ == "__main__":
    main()
