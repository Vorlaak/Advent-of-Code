def get_input() :
    #return("example.txt")
    return("input.txt")

def get_list(text) :
    with open(text) as file :
        data = file.read()
    return(data.split(' '))

def blink(stones) :
    new_stones = []
    for stone in stones :
        if int(stone) == 0 :
            new_stones.append('1')
        elif (len(stone)%2 == 0) :
            new_stones.append(str(int(stone[:(len(stone)//2)])))
            new_stones.append(str(int(stone[(len(stone)//2):])))
        else :
            new_stones.append(str(int(stone)*2024))
    return new_stones

def main() :
    textfile = get_input()
    stones = get_list(textfile)
    number_of_blinks = 25
    for _ in range(number_of_blinks) :
        stones = blink(stones)
    print(len(stones))

if __name__=="__main__":
    main()