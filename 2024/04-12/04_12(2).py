def get_input() :
    #return("example.txt")
    return("input.txt")

def main() :
    textfile = get_input()
    grid = get_grid(textfile)
    check_grid(grid=grid)

def get_grid(textfile) :
    with open(textfile) as file :
        grid = []
        for linestring in file :
            line = []
            for char in linestring :
                line.append(char)
            grid.append(line[:-1])
    return grid

def direction_1(grid, pos) :
    (x_pos, y_pos) = pos
    if (y_pos < 1) or (x_pos < 1) or ((len(grid) - y_pos) < 2) or ((len(grid[0]) - x_pos) < 2) or (grid[y_pos - 1][x_pos - 1] != 'M') or (grid[y_pos + 1][x_pos + 1] != 'S') or (grid[y_pos + 1][x_pos - 1] != 'M') or (grid[y_pos - 1][x_pos + 1] != 'S') :
        return False
    else :
        return True

def direction_2(grid, pos) :
    (x_pos, y_pos) = pos
    if (y_pos < 1) or (x_pos < 1) or ((len(grid) - y_pos) < 2) or ((len(grid[0]) - x_pos) < 2) or (grid[y_pos - 1][x_pos - 1] != 'M') or (grid[y_pos + 1][x_pos + 1] != 'S') or (grid[y_pos + 1][x_pos - 1] != 'S') or (grid[y_pos - 1][x_pos + 1] != 'M') :
        return False
    else :
        return True

def direction_3(grid, pos) :
    (x_pos, y_pos) = pos
    if (y_pos < 1) or (x_pos < 1) or ((len(grid) - y_pos) < 2) or ((len(grid[0]) - x_pos) < 2) or (grid[y_pos - 1][x_pos - 1] != 'S') or (grid[y_pos + 1][x_pos + 1] != 'M') or (grid[y_pos + 1][x_pos - 1] != 'M') or (grid[y_pos - 1][x_pos + 1] != 'S') :
        return False
    else :
        return True

def direction_4(grid, pos) :
    (x_pos, y_pos) = pos
    if (y_pos < 1) or (x_pos < 1) or ((len(grid) - y_pos) < 2) or ((len(grid[0]) - x_pos) < 2) or (grid[y_pos - 1][x_pos - 1] != 'S') or (grid[y_pos + 1][x_pos + 1] != 'M') or (grid[y_pos + 1][x_pos - 1] != 'S') or (grid[y_pos - 1][x_pos + 1] != 'M') :
        return False
    else :
        return True

def check_a(grid, pos) :
    count = 0
    directions = [direction_1(grid=grid, pos=pos),
                  direction_2(grid=grid, pos=pos),
                  direction_3(grid=grid, pos=pos),
                  direction_4(grid=grid, pos=pos)]
    for a in directions :
        if a :
            count += 1
    return(count)

def check_grid(grid) :
    sum = 0
    for y_char in range(len(grid)) :
        for x_char in range(len(grid[y_char])) :
            if grid[y_char][x_char] == 'A' :
                sum += check_a(grid=grid, pos=(x_char, y_char))
    print(sum)

if __name__=="__main__":
    main()