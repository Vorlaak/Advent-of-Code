from functools import lru_cache

def get_input() :
    return("example.txt")
    return("input.txt")

def get_towels(text) :
    with open(text) as file :
        data = file.read()
    [temp_1, temp_2] = data.split('\n\n')
    towels = temp_1.split(', ')
    patterns = temp_2.split('\n')
    return towels, patterns

towels, patterns = get_towels(get_input())

@lru_cache(maxsize=None)
def separate(pattern, length) :
    counter = 0
    for i in range(1, length + 1) :
        if len(pattern) == i :
            if pattern in towels :
                counter += 1
        elif (len(pattern) > i) and (pattern[:i] in towels) :
            counter += separate(pattern[i:], length)
    return counter


def is_possible(pattern, towels) :
    to_verify = []
    length_longer_pattern = 0
    for towel in towels :
        if towel in pattern :
            length_longer_pattern = max(length_longer_pattern, len(towel))
            to_verify.append(towel)
    return(separate(pattern, length_longer_pattern))

def main() :
    sum = 0
    for pattern in patterns :
        sum += is_possible(pattern, towels)
    print(sum)

if __name__=="__main__":
    main()