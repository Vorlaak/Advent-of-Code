def get_input() :
    return("example.txt")
    return("input.txt")

def get_grid(text) :
    start_position = (0, 0)
    start_direction = 0
    obstacles = []
    seen = []
    with open(text) as file :
        i = 0
        for line in file :
            data = line.split()
            for string_line in data :
                j = 0
                obstacles_line = []
                seen_line = []
                for element in string_line :
                    if element == '#' :
                        seen_line.append(False)
                        obstacles_line.append(True)
                        j += 1
                    elif element == '.' :
                        seen_line.append(False)
                        obstacles_line.append(False)
                        j += 1
                    elif element == '^' :
                        seen_line.append(True)
                        obstacles_line.append(False)
                        start_position = (i, j)
                        start_direction = 1
                        j += 1
                    elif element == '>' :
                        seen_line.append(True)
                        obstacles_line.append(False)
                        start_position = (i, j)
                        start_direction = 2
                        j += 1
                    elif element == 'v' :
                        seen_line.append(True)
                        obstacles_line.append(False)
                        start_position = (i, j)
                        start_direction = 3
                        j += 1
                    elif element == '<' :
                        seen_line.append(True)
                        obstacles_line.append(False)
                        start_position = (i, j)
                        start_direction = 4
                        j += 1
                obstacles.append(obstacles_line)
                seen.append(seen_line)
                i += 1
    return([seen, obstacles, start_position, start_direction])

def compute_move(seen, obstacles, position, direction) :
    match direction :
        case 1 :
            if position[0] == 0 :
                return([seen, position, 5])
            elif obstacles[position[0]-1][position[1]] :
                return([seen, position, 2])
            else :
                seen[position[0]-1][position[1]] = True
                return([seen, (position[0]-1, position[1]), direction])
        case 2 :
            if position[1] == (len(obstacles[0]) - 1) :
                return([seen, position, 5])
            elif obstacles[position[0]][position[1] + 1] :
                return([seen, position, 3])
            else :
                seen[position[0]][position[1] + 1] = True
                return([seen, (position[0], position[1] + 1), direction])
        case 3 :
            if position[0] == (len(obstacles) - 1) :
                return([seen, position, 5])
            elif obstacles[position[0]+1][position[1]] :
                return([seen, position, 4])
            else :
                seen[position[0]+1][position[1]] = True
                return([seen, (position[0]+1, position[1]), direction])
        case 4 :
            if position[1] == 0 :
                return([seen, position, 5])
            elif obstacles[position[0]][position[1] - 1] :
                return([seen, position, 1])
            else :
                seen[position[0]][position[1] - 1] = True
                return([seen, (position[0], position[1] - 1), direction])

def main() :
    textfile = get_input()
    [seen, obstacles, position, direction] = get_grid(textfile)
    while direction != 5 :
        [seen, position, direction] = compute_move(seen, obstacles, position, direction)
    sum = 0
    for line in seen :
        for place in line :
            if place :
                sum += 1
    print(sum)

if __name__=="__main__":
    main()