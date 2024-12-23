def get_input() :
    return("example.txt")
    return("input.txt")
 
def get_pattern(text) :
    numbers = []
    operations = []
    with open(text) as file :
        for line in file :
            data = line.split(': ')
            numbers.append(data[0])
            operations.append(data[1].split(' '))
            operations[-1][-1] = operations[-1][-1][:-1]
    return([numbers, operations])

def ter(n) :
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(reversed(nums))

def compute_line(number, operations) :
    operators = []
    for i in range(3**(len(operations)-1)) :
        operators.append(ter(i).zfill(len(operations)-1))
    flag = False
    for b in operators :
        sum = int(operations[0])
        for i in range(1, len(operations)) :
            if b[i-1] == '0' :
                sum += int(operations[i])
            elif b[i-1] == '1' :
                sum *= int(operations[i])
            elif b[i-1] == '2' :
                sum = int(str(sum) + operations[i])
        if sum == int(number) :
            flag = True
    if flag :
        return(int(number))
    else :
        return(0)

def main() :
    textfile = get_input()
    [numbers, operations] = get_pattern(textfile)
    big_sum = 0
    for i in range(len(numbers)) :
        big_sum += compute_line(numbers[i], operations[i])
    print(big_sum)

if __name__=="__main__":
    main()