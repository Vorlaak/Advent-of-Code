def get_input() :
    return("example.txt")
    return("input.txt")

def expand(text) :
    with open(text) as file :
        data = file.read()
    counter = 0
    blocks = []
    done = []
    flag = True
    for i in data :
        if flag :
            for _ in range(int(i)) :
                blocks.append(counter)
            done.append(False)
            counter += 1
            flag = False
        else :
            for _ in range(int(i)) :
                blocks.append('.')
            done.append(True)
            flag = True
    return([blocks, done])

def compact(blocks, done, text) :
    with open(text) as file :
        data = file.read()
    for i in range(len(done)) :
        if  not done[len(done)-i-1] :
            length = int(data[len(done)-i-1])
            counter = 0
            j = 0
            sum = 0
            for index in range(len(done)-i-1) :
                sum += int(data[index])
            while (j < len(blocks)) and (counter < length) and (j <= sum):
                if blocks[j] == '.' :
                    counter += 1
                    j += 1
                else :
                    counter = 0
                    j +=1
            if counter != 0 :
                for k in range(length) :
                    blocks[j-length+k] = (len(done)-i-1)//2
                    blocks[sum + k] = '.'
            done[len(done)-i-1] = True
    return blocks

def main() :
    textfile = get_input()
    [blocks, done] = expand(textfile)
    blocks = compact(blocks, done, textfile)
    sum = 0
    for i in range(len(blocks)) :
        if isinstance(blocks[i], int) :
            sum += (i * blocks[i])
    print(sum)

if __name__=="__main__":
    main()