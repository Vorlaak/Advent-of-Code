def get_input() :
    return("example.txt")
    return("input.txt")

def get_grid(textfile) :
    with open(textfile) as file :
        grid = []
        for linestring in file :
            line = []
            for char in linestring :
                line.append(char)
            grid.append(line[:-1])
    for i in range(len(grid)) :
        for j in range(len(grid[i])) :
            grid[i][j] = int(grid[i][j])
    return grid

def check_direction_up(pose, grid) :
    (y, x) = pose
    if (y == 0) :
        return (0, pose)
    elif (grid[y - 1][x] == 9) and (grid[y][x] == 8) :
        return (2, (y - 1, x))
    elif grid[y - 1][x] == (grid[y][x] + 1) :
        return (1, (y - 1, x))
    else :
        return (0, pose)

def check_direction_right(pose, grid) :
    (y, x) = pose
    if (x == (len(grid[y]) - 1)) :
        return (0, pose)
    elif (grid[y][x + 1] == 9) and (grid[y][x] == 8) :
        return (2, (y, x + 1))
    elif grid[y][x + 1] == (grid[y][x] + 1) :
        return (1, (y, x + 1))
    else :
        return (0, pose)

def check_direction_down(pose, grid) :
    (y, x) = pose
    if (y == (len(grid) - 1)) :
        return (0, pose)
    elif (grid[y + 1][x] == 9) and (grid[y][x] == 8) :
        return (2, (y + 1, x))
    elif grid[y + 1][x] == (grid[y][x] + 1) :
        return (1, (y + 1, x))
    else :
        return (0, pose)

def check_direction_left(pose, grid) :
    (y, x) = pose
    if (x == 0) :
        return (0, pose)
    elif (grid[y][x - 1] == 9) and (grid[y][x] == 8) :
        return (2, (y, x - 1))
    elif grid[y][x - 1] == (grid[y][x] + 1) :
        return (1, (y, x - 1))
    else :
        return (0, pose)

def check_directions(pose, grid) :
    to_check = [pose]
    final_positions = []
    while len(to_check) > 0 :
        test = to_check.pop(0)
        directions = []
        directions.append(check_direction_up(test, grid))
        directions.append(check_direction_right(test, grid))
        directions.append(check_direction_down(test, grid))
        directions.append(check_direction_left(test, grid))
        for i in directions :
            if i[0] == 1 :
                to_check.append(i[1])
            elif i[0] == 2 :
                final_positions.append(i[1])
    return len(final_positions)
    
def main() :
    textfile = get_input()
    grid = get_grid(textfile)
    sum = 0
    for line in range(len(grid)) :
        for element in range(len(grid[line])) :
            if grid[line][element] == 0 :
                sum += check_directions((line, element), grid)
    print(sum)

if __name__=="__main__":
    main()