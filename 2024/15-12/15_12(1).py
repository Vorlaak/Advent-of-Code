def get_input() :
    return("example.txt")
    return("input.txt")

def get_grid(text) :
    with open(text) as file :
        data = file.read()
    [obstacles, moves] = data.split("\n\n")
    start_position = (0, 0)
    grid = []
    lines = obstacles.split("\n")
    for i in range(len(lines)) :
        line_list = []
        for j in range(len(lines[i])) :
            if lines[i][j] == "#" :
                line_list.append(2)
            elif lines[i][j] == "." :
                line_list.append(0)
            elif lines[i][j] == "O" :
                line_list.append(1)
            elif lines[i][j] == "@" :
                start_position = (i, j)
                line_list.append(0)
        grid.append(line_list)
    return grid, start_position, moves

def push(grid, position, direction) :
    (y_pose, x_pose) = position
    match direction :
        case 0 :
            match grid[y_pose - 1][x_pose] :
                case 2 :
                    return(False, grid) 
                case 1 :
                    return(push(grid, (y_pose - 1, x_pose), direction))
                case 0 :
                    grid[y_pose - 1][x_pose] = 1
                    return(True, grid)
        case 1 :
            match grid[y_pose][x_pose + 1] :
                case 2 :
                    return(False, grid) 
                case 1 :
                    return(push(grid, (y_pose, x_pose + 1), direction))
                case 0 :
                    grid[y_pose][x_pose + 1] = 1
                    return(True, grid)
        case 2 :
            match grid[y_pose + 1][x_pose] :
                case 2 :
                    return(False, grid) 
                case 1 :
                    return(push(grid, (y_pose + 1, x_pose), direction))
                case 0 :
                    grid[y_pose + 1][x_pose] = 1
                    return(True, grid)
        case 3 :
            match grid[y_pose][x_pose - 1] :
                case 2 :
                    return(False, grid) 
                case 1 :
                    return(push(grid, (y_pose, x_pose - 1), direction))
                case 0 :
                    grid[y_pose][x_pose - 1] = 1
                    return(True, grid)

def move(grid, position, direction) :
    (y_pose, x_pose) = position
    match direction :
        case 0 :
            match grid[y_pose - 1][x_pose] :
                case 2 :
                    return (False, grid)
                case  1 :
                    (pushed, new_grid) = push(grid, (y_pose - 1, x_pose), direction)
                    if pushed :
                        new_grid[y_pose - 1][x_pose] = 0
                        return(True, new_grid)
                    else :
                        return(False, new_grid)
                case 0 :
                    return (True, grid)
        case 1 :
            match grid[y_pose][x_pose + 1] :
                case 2 :
                    return (False, grid)
                case 1 :
                    (pushed, new_grid) = push(grid, (y_pose, x_pose + 1), direction)
                    if pushed :
                        new_grid[y_pose][x_pose + 1] = 0
                        return(True, new_grid)
                    else :
                        return(False, new_grid)
                case 0 :
                    return (True, grid)
        case 2 :
            match grid[y_pose + 1][x_pose] :
                case 2 :
                    return (False, grid)
                case 1 :
                    (pushed, new_grid) = push(grid, (y_pose + 1, x_pose), direction)
                    if pushed :
                        new_grid[y_pose + 1][x_pose] = 0
                        return(True, new_grid)
                    else :
                        return(False, new_grid)
                case 0 :
                    return (True, grid)
        case 3 :
            match grid[y_pose][x_pose - 1] :
                case 2 :
                    return (False, grid)
                case 1 :
                    (pushed, new_grid) = push(grid, (y_pose, x_pose - 1), direction)
                    if pushed :
                        new_grid[y_pose][x_pose - 1] = 0
                        return(True, new_grid)
                    else :
                        return(False, new_grid)
                case 0 :
                    return (True, grid)

def compute_moves(grid, position, moves) :
    (y_pose, x_pose) = position
    for direction in moves :
        match direction :
            case '^' :
                (moved, grid) = move(grid, (y_pose, x_pose), 0)
                if moved :
                    y_pose -= 1
            case '>' :
                (moved, grid) = move(grid, (y_pose, x_pose), 1)
                if moved :
                    x_pose += 1
            case 'v' :
                (moved, grid) = move(grid, (y_pose, x_pose), 2)
                if moved :
                    y_pose += 1
            case '<' :
                (moved, grid) = move(grid, (y_pose, x_pose), 3)
                if moved :
                    x_pose -= 1
    return grid
                

def main() :
    textfile = get_input()
    grid, start_position, moves = get_grid(textfile)
    def_grid = compute_moves(grid, start_position, moves)
    sum = 0
    for y in range(len(def_grid)) :
        for x in range(len(def_grid[y])) :
            if def_grid[y][x] == 1 :
                sum += (100*y + x)
    print(sum)
    

if __name__=="__main__":
    main()