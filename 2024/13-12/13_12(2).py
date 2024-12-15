import re
from functools import lru_cache

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

@lru_cache(maxsize=None)
def decompose(a_1, a_2, b_1, b_2, p_1, p_2) :
    i = (p_1*b_2 - p_2*b_1) / (a_1*b_2 - a_2*b_1)
    j = (a_1*p_2 - a_2*p_1) / (a_1*b_2 - a_2*b_1)
    if i == int(i) and j == int(j) :
        return (3*int(i) + int(j))
    else :
        return 0

def calculate_machine(machine) :
    (A, B, prize) = machine
    prize[0] = 10000000000000 + prize[0]
    prize[1] = 10000000000000 + prize[1]
    return decompose(A[0], A[1], B[0], B[1], prize[0], prize[1])
        
def main() :
    textfile = get_input()
    machines = get_machines(textfile)
    sum = 0
    for machine in machines :
        sum += calculate_machine(machine)
    print(sum)

if __name__=="__main__":
    main()