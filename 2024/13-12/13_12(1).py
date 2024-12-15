import re

def get_input() :
    #return("example.txt")
    return("input.txt")

def get_machines(text) :
    pattern = r'\d+'
    with open(text) as file :
        data = file.read()
    machines = data.split('\n\n')
    for i in range(len(machines)) :
        machines[i] = machines[i].split('\n')
        for j in range(len(machines[i])) :
            machines[i][j] = re.findall(pattern, machines[i][j])
            for k in range(len(machines[i][j])) :
                machines[i][j][k] = int(machines[i][j][k])
    return machines

def calculate_machine(machine) :
    (A, B, prize) = machine
    min_price = 401
    flag = False
    for i in range(101) :
        for j in range(101) :
            if (i*A[0] + j*B[0] == prize[0]) and (i*A[1] + j*B[1] == prize[1]) :
                flag = True
                price = 3*i + j
                if price < min_price :
                    min_price = price
    if flag :
        return min_price
    else :
        return 0
        
def main() :
    textfile = get_input()
    machines = get_machines(textfile)
    sum = 0
    for machine in machines :
        sum += calculate_machine(machine)
    print(sum)

if __name__=="__main__":
    main()