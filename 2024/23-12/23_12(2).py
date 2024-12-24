import random

def get_input() :
    #return("example.txt")
    return("input.txt")

def get_networks(text) :
    with open(text) as file :
        data = file.read().split('\n')
    dict = {}
    for line in data :
        pc_1 = line[0] + line[1]
        pc_2 = line[-2] + line[-1]
        if pc_1 not in dict :
            dict[pc_1] = [pc_2]
        elif pc_2 not in dict[pc_1] :
            dict[pc_1].append(pc_2)
        if pc_2 not in dict :
            dict[pc_2] = [pc_1]
        elif pc_1 not in dict[pc_2] :
            dict[pc_2].append(pc_1)
    vertices = list(dict.keys())
    number_of_vertices = len(dict)
    grid = [[0 for _ in range(number_of_vertices)] for _ in range(number_of_vertices)]
    for i in range(number_of_vertices) :
        neighbors = dict[vertices[i]]
        for j in range(len(neighbors)) :
            index = vertices.index(neighbors[j])
            grid[i][index] = 1
            grid[index][i] = 1
    return grid, vertices

def BronKerbosch2(P, R=None, X=None):
    P = set(P)
    R = set() if R is None else R
    X = set() if X is None else X
    if not P and not X:
        yield R
    try:
        u = random.choice(list(P.union(X)))
        S = P.difference(N[u])
    # if union of P and X is empty
    except IndexError:
        S = P
    for v in S:
        yield from BronKerbosch2(
            P=P.intersection(N[v]), R=R.union([v]), X=X.intersection(N[v]))
        P.remove(v)
        X.add(v)

def main() :
    textfile = get_input()
    grid, vertices = get_networks(textfile)
    global N
    N = {
    i: set(num for num, j in enumerate(row) if j)
    for i, row in enumerate(grid)
    }
    P = N.keys()
    cliques = list(BronKerbosch2(P))
    maxi = 0
    max_clique = {}
    for clique in cliques :
        if len(clique) > maxi :
            maxi = len(clique)
            max_clique = clique
    good_net = []
    for vertex in max_clique :
        good_net.append(vertices[vertex])
    print(",".join(sorted(good_net)))
    
if __name__=="__main__":
    main()