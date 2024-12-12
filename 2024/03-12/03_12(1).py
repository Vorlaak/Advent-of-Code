import re

def get_input() :
    #return("example.txt")
    return("input.txt")

def parse_text(text) :
    sum = 0
    pattern = r'mul\(([0-9]*),([0-9]*)\)'
    with open(text, 'r') as file :
        data = file.read().replace('\n','')
        for (numb_1, numb_2) in re.findall(pattern, data) :
            sum += (int(numb_1) * int(numb_2))
    print(sum)

def main() :
    textfile = get_input()
    parse_text(textfile)

if __name__=="__main__":
    main()