def get_input() :
    #return("example.txt")
    return("input.txt")

def process_report(report) :
    flag = report[0] < report[1]
    if flag :
        for i in range(len(report) - 1) :
            if (report[i] >= report[i + 1]) or ((report[i + 1] - report[i]) > 3) :
                return False
        return True
    else :
        for i in range(len(report) - 1) :
            if (report[i] <= report[i + 1]) or ((report[i] - report[i + 1]) > 3) :
                return False
        return True

def get_good_reports(text) :
    count = 0
    with open(text) as file :
        for line in file :
            data = line.split()
            report = []
            for i in range(len(data)) :
                try :
                    if isinstance(int(data[i]), int) :
                        report.append(int(data[i]))
                except (IndexError, ValueError) as _ :
                    pass
            if process_report(report) :
                count += 1
    return count

def main() :
    textfile = get_input()
    print(get_good_reports(textfile))

if __name__=="__main__":
    main()