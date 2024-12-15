from functools import lru_cache

def get_input() :
    #return("example.txt")
    return("input.txt")

def get_list(text) :
    with open(text) as file :
        data = file.read()
    return(data.split(' '))

@lru_cache(maxsize=None)
def blink(stone, depth, number_of_blinks) :
    if depth == number_of_blinks :
        return 1

    if int(stone) == 0 :
        return(blink('1', depth+1, number_of_blinks))
    elif (len(stone)%2 == 0) :
        return(blink(str(int(stone[:(len(stone)//2)])), depth+1, number_of_blinks) 
              +blink(str(int(stone[(len(stone)//2):])), depth+1, number_of_blinks))
    else :
        return(blink(str(int(stone)*2024), depth+1, number_of_blinks))

def main() :
    textfile = get_input()
    stones = get_list(textfile)
    number_of_blinks = 75
    sum = 0
    for stone in stones :
        sum += blink(stone, 0, number_of_blinks)
    print(sum)

if __name__=="__main__":
    main()