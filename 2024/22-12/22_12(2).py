from tqdm import tqdm

def get_input() :
    #return("example.txt")
    return("input.txt")

def get_codes(text) :
    with open(text) as file :
        data = file.read().split('\n')
    return data

def new_secret_number(sec_num) :
    dict = {}
    prev = int(str(sec_num)[-1])
    seq = [prev]
    for _ in range(3) :
        sec_num = ((sec_num * 64) ^ sec_num) % 16777216
        sec_num = ((int(sec_num/32)) ^ sec_num) % 16777216
        sec_num = ((sec_num * 2048) ^ sec_num) % 16777216
        num = int(str(sec_num)[-1])
        change = num - prev
        prev = int(str(sec_num)[-1])
        seq.append(change)
        price = num
    dict[tuple(seq)] = price
    for _ in range(1997) :
        sec_num = ((sec_num * 64) ^ sec_num) % 16777216
        sec_num = ((int(sec_num/32)) ^ sec_num) % 16777216
        sec_num = ((sec_num * 2048) ^ sec_num) % 16777216
        num = int(str(sec_num)[-1])
        change = num - prev
        prev = int(str(sec_num)[-1])
        _ = seq.pop(0)
        seq.append(change)
        price = num
        if tuple(seq) not in dict :
            dict[tuple(seq)] = price
    return dict

def sequence(seq_0, seq_1, seq_2, seq_3) :
    sum = 0
    seq = (seq_0, seq_1, seq_2, seq_3)
    for i in range(len(price_changes)) :
        if seq in price_changes[i] :
            sum += price_changes[i][seq]
    return sum
    
def main() :
    textfile = get_input()
    initial_secret_numbers = get_codes(textfile)
    global price_changes
    price_changes = []
    max_bananas = 0
    for secret_number in initial_secret_numbers :
        secret_number = int(secret_number)
        dict = new_secret_number(secret_number)
        price_changes.append(dict)
    for h in tqdm(range(-9, 10)) :
        for i in range(-9, 10) :
            for j in range(-9, 10) :
                for k in range(-9, 10) :
                    max_bananas = max(max_bananas, sequence(h, i, j, k))
    print(max_bananas)

if __name__=="__main__":
    main()