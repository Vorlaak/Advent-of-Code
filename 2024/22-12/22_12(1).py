def get_input() :
    #return("example.txt")
    return("input.txt")

def get_codes(text) :
    with open(text) as file :
        data = file.read().split('\n')
    return data

def new_secret_number(sec_num, depth) :
    sec_num = ((sec_num * 64) ^ sec_num) % 16777216
    sec_num = ((int(sec_num/32)) ^ sec_num) % 16777216
    sec_num = ((sec_num * 2048) ^ sec_num) % 16777216
    return sec_num
    

def main() :
    textfile = get_input()
    initial_secret_numbers = get_codes(textfile)
    sum = 0
    for secret_number in initial_secret_numbers :
        secret_number = int(secret_number)
        for _ in range(2000) :
            secret_number = new_secret_number(secret_number, 2000)
        sum += secret_number
    print(sum)
    
if __name__=="__main__":
    main()