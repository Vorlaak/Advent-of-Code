def get_input():
    # return "example.txt"
    return "input.txt"


def get_lists(text, bank_list):
    with open(text) as file:
        for line in file:
            data = line.split()[0]
            bank_list.append(data)


def process_bank(bank):
    num = []
    prev = -1
    for i in range(12):
        index_max = max(range(prev + 1, len(bank) - 11 + i), key=bank.__getitem__)
        prev = index_max
        num.append(bank[index_max])
    res = 0
    count = 11
    for n in num:
        res += (10**count) * int(n)
        count -= 1
    return res


def main():
    textfile = get_input()
    bank_list = []
    get_lists(textfile, bank_list=bank_list)
    res = 0
    for bank in bank_list:
        res += process_bank(bank)
    print(res)


if __name__ == "__main__":
    main()
