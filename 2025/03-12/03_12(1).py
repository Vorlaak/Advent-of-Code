def get_input():
    # return "example.txt"
    return "input.txt"


def get_lists(text, bank_list):
    with open(text) as file:
        for line in file:
            data = line.split()[0]
            bank_list.append(data)


def process_bank(bank):
    maxi = 0
    max_left = -1
    for i in range(len(bank) - 1):
        if int(bank[i]) > max_left:
            max_left = int(bank[i])
            for j in range(i + 1, len(bank)):
                maxi = max(maxi, 10 * int(bank[i]) + int(bank[j]))
    return maxi


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
