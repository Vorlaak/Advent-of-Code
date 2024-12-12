import re

def get_input() :
    #return("example.txt")
    return("input.txt")

def parse_text(text) :
    pattern = r'mul\([0-9]*,[0-9]*\)|do\(\)|don\'t\(\)'
    with open(text, 'r') as file :
        data = file.read().replace('\n','')
        return(re.findall(pattern, data))

def process_multip(input) :
    flag = True
    sum = 0
    for match in input :
        if match == 'do()' :
            flag = True
        elif match == "don't()" :
            flag = False
        else :
            if flag :
                pat = r'mul\(([0-9]*),([0-9]*)\)'
                for (numb_1, numb_2) in re.findall(pat, match) :
                    sum += (int(numb_1) * int(numb_2))
    print(sum)

def main() :
    textfile = get_input()
    process_multip(parse_text(textfile))


if __name__=="__main__":
    main()