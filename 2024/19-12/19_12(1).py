def get_input() :
    #return("example.txt")
    return("input.txt")

def get_towels(text) :
    with open(text) as file :
        data = file.read()
    [temp_1, temp_2] = data.split('\n\n')
    towels = temp_1.split(', ')
    patterns = temp_2.split('\n')
    return towels, patterns

def check_towel(pattern, towel, pointer) :
    for i in range(len(towel)) :
        if (pointer + i == len(pattern)) or (towel[i] != pattern[i + pointer]) :
            return False
    return True

def ind_max(lis) :
    index = 0
    maxi = lis[0][1]
    for i, to_check in enumerate(lis) :
        _, length = to_check
        if length > maxi :
            maxi = length
            index = i
    return index

def is_possible(pattern, towels) :
    to_check = [([], 0)]
    while len(to_check) > 0 :
        towel_list, pointer = to_check.pop(ind_max(to_check))
        if pointer == len(pattern) :
            return True
        else :
            for towel in towels :
                if check_towel(pattern, towel, pointer) :
                    current_list = [a for a in towel_list]
                    current_list.append(towel)
                    to_check.append((current_list, pointer + len(towel)))
    return False

def main() :
    textfile = get_input()
    towels, patterns = get_towels(textfile)
    counter = 0
    for pattern in patterns :
        print(counter)
        if is_possible(pattern, towels) :
            counter += 1
    print(counter)

if __name__=="__main__":
    main()