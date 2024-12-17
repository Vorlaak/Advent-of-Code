def get_input() :
    #return("example.txt")
    return("input.txt")

def parse_input(text) :
    with open(text) as file :
        data = file.read()
    [registers, program] = data.split('\n\n')
    [A, B, C] = registers.split('\n')
    A = int(A.split(' ')[-1])
    B = int(B.split(' ')[-1])
    C = int(C.split(' ')[-1])
    numbers = program.split(' ')[-1].split(',')
    for i, number in enumerate(numbers) :
        numbers[i] = int(number)
    return A, B, C, numbers

def combo(num, A, B, C) :
    match num :
        case 0 :
            return 0
        case 1 :
            return 1
        case 2 :
            return 2
        case 3 :
            return 3
        case 4 :
            return A
        case 5 :
            return B
        case 6 :
            return C
        case 7 :
            return False

def main() :
    textfile = get_input()
    A, B, C, program = parse_input(textfile)
    pointer = 0
    output = []
    while pointer < len(program) :
        match program[pointer] :
            case 0 :
                A = int(A / (2**combo(program[pointer+1], A, B, C)))
                pointer += 2
            case 1 :
                B = B ^ program[pointer+1]
                pointer += 2
            case 2 :
                B = combo(program[pointer+1], A, B, C) % 8
                pointer += 2
            case 3 :
                if A != 0 :
                    pointer = program[pointer+1]
                else :
                    pointer += 2
            case 4 :
                B = B ^ C
                pointer += 2
            case 5 :
                output.append(str(combo(program[pointer+1], A, B, C) % 8))
                pointer += 2
            case 6 :
                B = int(A / (2**combo(program[pointer+1], A, B, C)))
                pointer += 2
            case 7 :
                C = int(A / (2**combo(program[pointer+1], A, B, C)))
                pointer += 2
    print(','.join(output))
if __name__=="__main__":
    main()