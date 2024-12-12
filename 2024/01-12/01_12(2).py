def get_input() :
    #return("example.txt")
    return("input.txt")

def get_lists(text, list_1, list_2) :
    with open(text) as file :
        for line in file :
            data = line.split()
            try :
                if isinstance(int(data[0]), int) :
                    list_1.append(int(data[0]))
                if isinstance(int(data[1]), int) :
                    list_2.append(int(data[1]))
            except (IndexError, ValueError) as _ :
                pass

def main() :
    textfile = get_input()
    list_1, list_2 = [], []
    get_lists(textfile, list_1=list_1, list_2=list_2)
    sum = 0
    for number in list_1 :
        count = 0
        for similar in list_2 :
            if number == similar :
                count += 1
        sum += (number * count)
    print(sum)

if __name__=="__main__":
    main()