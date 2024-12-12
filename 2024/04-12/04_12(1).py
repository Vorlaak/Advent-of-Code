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
    if (y_pos < 3) or (grid[y_pos - 1][x_pos] != 'M') or (grid[y_pos - 2][x_pos] != 'A') or (grid[y_pos - 3][x_pos] != 'S') :
        return False
    else :
        return True

def direction_2(grid, pos) :
    (x_pos, y_pos) = pos
    if (y_pos < 3) or ((len(grid[0]) - x_pos) < 4) or (grid[y_pos - 1][x_pos + 1] != 'M') or (grid[y_pos - 2][x_pos + 2] != 'A') or (grid[y_pos - 3][x_pos + 3] != 'S') :
        return False
    else :
        return True

def direction_3(grid, pos) :
    (x_pos, y_pos) = pos
    if ((len(grid[0]) - x_pos) < 4) or (grid[y_pos][x_pos + 1] != 'M') or (grid[y_pos][x_pos + 2] != 'A') or (grid[y_pos][x_pos + 3] != 'S') :
        return False
    else :
        return True

def direction_4(grid, pos) :
    (x_pos, y_pos) = pos
    if ((len(grid) - y_pos) < 4) or ((len(grid[0]) - x_pos) < 4) or (grid[y_pos + 1][x_pos + 1] != 'M') or (grid[y_pos + 2][x_pos + 2] != 'A') or (grid[y_pos + 3][x_pos + 3] != 'S') :
        return False
    else :
        return True
    
def direction_5(grid, pos) :
    (x_pos, y_pos) = pos
    if ((len(grid) - y_pos) < 4) or (grid[y_pos + 1][x_pos] != 'M') or (grid[y_pos + 2][x_pos] != 'A') or (grid[y_pos + 3][x_pos] != 'S') :
        return False
    else :
        return True

def direction_6(grid, pos) :
    (x_pos, y_pos) = pos
    if (x_pos < 3) or ((len(grid) - y_pos) < 4) or (grid[y_pos + 1][x_pos - 1] != 'M') or (grid[y_pos + 2][x_pos - 2] != 'A') or (grid[y_pos + 3][x_pos - 3] != 'S') :
        return False
    else :
        return True

def direction_7(grid, pos) :
    (x_pos, y_pos) = pos
    if (x_pos < 3) or (grid[y_pos][x_pos - 1] != 'M') or (grid[y_pos][x_pos - 2] != 'A') or (grid[y_pos][x_pos - 3] != 'S') :
        return False
    else :
        return True
    
def direction_8(grid, pos) :
    (x_pos, y_pos) = pos
    if (x_pos < 3) or (y_pos < 3) or (grid[y_pos - 1][x_pos - 1] != 'M') or (grid[y_pos - 2][x_pos - 2] != 'A') or (grid[y_pos - 3][x_pos - 3] != 'S') :
        return False
    else :
        return True

def check_x(grid, pos) :
    count = 0
    directions = [direction_1(grid=grid, pos=pos),
                  direction_2(grid=grid, pos=pos),
                  direction_3(grid=grid, pos=pos),
                  direction_4(grid=grid, pos=pos),
                  direction_5(grid=grid, pos=pos),
                  direction_6(grid=grid, pos=pos),
                  direction_7(grid=grid, pos=pos),
                  direction_8(grid=grid, pos=pos)]
    for a in directions :
        if a :
            count += 1
    return(count)

def check_grid(grid) :
    sum = 0
    for y_char in range(len(grid)) :
        for x_char in range(len(grid[y_char])) :
            if grid[y_char][x_char] == 'X' :
                sum += check_x(grid=grid, pos=(x_char, y_char))
    print(sum)

if __name__=="__main__":
    main()