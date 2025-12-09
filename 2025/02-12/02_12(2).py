def get_input():
    # return "example.txt"
    return "input.txt"


def get_lists(text, range_list):
    with open(text) as file:
        ranges = file.read().split(",")
        for range in ranges:
            range_list.append((int(range.split("-")[0]), int(range.split("-")[1])))


def is_repeating(num):
    word = str(num)
    length = len(word)
    for i in range(1, length // 2 + 1):
        new_length = 0
        new_word = ""
        while new_length < length:
            new_word += word[:i]
            new_length += i
        if new_word == word:
            return True
    return False


def process_range(start, finish):
    counter = 0
    for i in range(start, finish + 1):
        if is_repeating(i):
            counter += i
    return counter


def main():
    textfile = get_input()
    range_list = []
    get_lists(textfile, range_list=range_list)
    counter = 0
    for range in range_list:
        counter += process_range(range[0], range[1])
    print(counter)


if __name__ == "__main__":
    main()
