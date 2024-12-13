def get_input() :
    return("example.txt")
    return("input.txt")

def get_grid(text) :
    seen = []
    frequencies = []
    antennas = []
    with open(text) as file :
        i = 0
        for line in file :
            data = line.split()
            for string_line in data :
                j = 0
                seen_line = []
                for element in string_line :
                    if element == '.' :
                        seen_line.append(False)
                        j += 1
                    else :
                        seen_line.append(True)
                        if element in frequencies :
                            antennas[frequencies.index(element)].append((i,j))
                        else :
                            frequencies.append(element)
                            antennas.append([(i, j)])
                        j += 1
                seen.append(seen_line)
                i += 1
    return([frequencies, antennas, seen])

def in_grid(position, grid) :
    (i, j) = position
    if (i<0) or (j<0) or (i>=len(grid)) or (j>=len(grid[0])) :
        return False
    else :
        return True

def process_frequencies(frequencies, antennas, seen) :
    for i in range(len(frequencies)) :
        for j in range(len(antennas[i])-1) :
            for k in range(j+1, len(antennas[i])) :
                (diff_y, diff_x) = (antennas[i][k][0] - antennas[i][j][0], antennas[i][k][1] - antennas[i][j][1])
                count_1 = 1
                count_2 = 1
                flag_1 = True
                flag_2 = True
                while flag_1 :
                    if in_grid((antennas[i][j][0]-(count_1 * diff_y), antennas[i][j][1]-(count_1 * diff_x)), seen) :
                        seen[antennas[i][j][0]-(count_1 * diff_y)][antennas[i][j][1]-(count_1 * diff_x)] = True
                        count_1+=1
                    else :
                        flag_1 = False
                while flag_2 :
                    if in_grid((antennas[i][k][0]+(count_2 * diff_y), antennas[i][k][1]+(count_2 * diff_x)), seen) :
                        seen[antennas[i][k][0]+(count_2 * diff_y)][antennas[i][k][1]+(count_2 * diff_x)] = True
                        count_2 += 1
                    else :
                        flag_2 = False
    return(seen)

def main() :
    textfile = get_input()
    [frequencies, antennas, seen] = get_grid(textfile)
    seen = process_frequencies(frequencies, antennas, seen)
    sum = 0
    for line in seen :
        for element in line :
            if element :
                sum += 1
    print(sum)

if __name__=="__main__":
    main()