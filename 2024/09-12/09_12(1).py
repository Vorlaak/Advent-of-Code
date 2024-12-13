def get_input() :
    #return("example.txt")
    return("input.txt")

def expand(text) :
    with open(text) as file :
        data = file.read()
    counter = 0
    blocks = []
    flag = True
    for i in data :
        if flag :
            for _ in range(int(i)) :
                blocks.append(counter)
            counter += 1
            flag = False
        else :
            for _ in range(int(i)) :
                blocks.append('.')
            flag = True
    return blocks

def compact(blocks) :
    j = len(blocks) - 1
    while j >= 0 :
        if blocks[j] != '.' :
            i = 0
            while blocks[i] != '.' :
                i += 1
            if i < j :
                blocks[i] = blocks[j]
                blocks[j] = '.'
            j -= 1
        else :
            j -= 1
    return blocks

def main() :
    textfile = get_input()
    blocks = compact(expand(textfile))
    sum = 0
    for i in range(len(blocks)) :
        if isinstance(blocks[i], int) :
            sum += (i * blocks[i])
    print(sum)

if __name__=="__main__":
    main()