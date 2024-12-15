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
    for y in range(len(lines)) :
        line_list = []
        for x in range(len(lines[y])) :
            if lines[y][x] == "#" :
                line_list.append(2)
                line_list.append(2)
            elif lines[y][x] == "." :
                line_list.append(0)
                line_list.append(0)
            elif lines[y][x] == "O" :
                line_list.append(3)
                line_list.append(4)
            elif lines[y][x] == "@" :
                start_position = (y, 2*x)
                line_list.append(0)
                line_list.append(0)
        grid.append(line_list)
    return grid, start_position, moves

def push(grid, position, direction) :
    (y_pose, x_pose) = position
    match direction :
        case 0 :
            match grid[y_pose - 1][x_pose] :
                case 4 :
                    return(push(grid, (y_pose - 1, x_pose - 1), direction) and (push(grid, (y_pose - 1, x_pose), direction)))
                case 3 :
                    return(push(grid, (y_pose - 1, x_pose), direction) and (push(grid, (y_pose - 1, x_pose + 1), direction)))
                case 2 :
                    return(False) 
                case 0 :
                    return(True)
        case 1 :
            match grid[y_pose][x_pose + 1] :
                case 3 :
                    return(push(grid, (y_pose, x_pose + 2), direction))
                case 2 :
                    return(False) 
                case 0 :
                    return(True)
        case 2 :
            match grid[y_pose + 1][x_pose] :
                case 4 :
                    return(push(grid, (y_pose + 1, x_pose - 1), direction) and (push(grid, (y_pose + 1, x_pose), direction)))
                case 3 :
                    return(push(grid, (y_pose + 1, x_pose), direction) and (push(grid, (y_pose + 1, x_pose + 1), direction)))
                case 2 :
                    return(False)
                case 0 :
                    return(True)
        case 3 :
            match grid[y_pose][x_pose - 1] :
                case 4 :
                    return(push(grid, (y_pose, x_pose - 2), direction))
                case 2 :
                    return(False) 
                case 0 :
                    return(True)
    
def push_box(grid, pose_1, pose_2, direction) :
    match direction :
        case 0 :
            can_move = push(grid, pose_1, direction) and push(grid, pose_2, direction)
            if can_move :
                new_grid = force_move(grid, pose_1, direction, 0)
                grid = force_move(new_grid, pose_2, direction, 0)
                return (True, grid)
            else :
                return(False, grid)
        case 1 :
            can_move = push(grid, pose_2, direction)
            if can_move :
                new_grid = force_move(grid, pose_2, direction, 0)
                grid = force_move(new_grid, pose_1, direction, 0)
                return (True, grid)
            else :
                return(False, grid)
        case 2 :
            can_move = push(grid, pose_1, direction) and push(grid, pose_2, direction)
            if can_move :
                new_grid = force_move(grid, pose_1, direction, 0)
                grid = force_move(new_grid, pose_2, direction, 0)
                return (True, grid)
            else :
                return(False, grid)
        case 3 :
            can_move = push(grid, pose_1, direction)
            if can_move :
                new_grid = force_move(grid, pose_1, direction, 0)
                grid = force_move(new_grid, pose_2, direction, 0)
                return (True, grid)
            else :
                return(False, grid)

def force_move(grid, pose, direction, previous) :
    (y_pose, x_pose) = pose
    match direction :
        case 0 :
            match grid[y_pose][x_pose] :
                case 0 :
                    grid[y_pose][x_pose] = previous
                    return grid
                case 3 :
                    grid[y_pose][x_pose] = previous
                    if previous == 4 :
                        grid = force_move(grid, (y_pose, x_pose + 1), direction, 0)
                        return(force_move(grid, (y_pose - 1, x_pose), direction, 3))
                    return(force_move(grid, (y_pose - 1, x_pose), direction, 3))
                case 4 :
                    grid[y_pose][x_pose] = previous
                    if previous == 3 :
                        grid = force_move(grid, (y_pose, x_pose - 1), direction, 0)
                        return(force_move(grid, (y_pose - 1, x_pose), direction, 4))
                    return(force_move(grid, (y_pose - 1, x_pose), direction, 4))
        case 1 :
            match grid[y_pose][x_pose] :
                case 0 :
                    grid[y_pose][x_pose] = previous
                    return grid
                case 3 :
                    grid[y_pose][x_pose] = previous
                    return(force_move(grid, (y_pose, x_pose + 1), direction, 3))
                case 4 :
                    grid[y_pose][x_pose] = previous
                    return(force_move(grid, (y_pose, x_pose + 1), direction, 4))
        case 2 :
            match grid[y_pose][x_pose] :
                case 0 :
                    grid[y_pose][x_pose] = previous
                    return grid
                case 3 :
                    grid[y_pose][x_pose] = previous
                    if previous == 4 :
                        grid = force_move(grid, (y_pose, x_pose + 1), direction, 0)
                        return(force_move(grid, (y_pose + 1, x_pose), direction, 3))
                    return(force_move(grid, (y_pose + 1, x_pose), direction, 3))
                case 4 :
                    grid[y_pose][x_pose] = previous
                    if previous == 3 :
                        grid = force_move(grid, (y_pose, x_pose - 1), direction, 0)
                        return(force_move(grid, (y_pose + 1, x_pose), direction, 4))
                    return(force_move(grid, (y_pose + 1, x_pose), direction, 4))
        case 3 :
            match grid[y_pose][x_pose] :
                case 0 :
                    grid[y_pose][x_pose] = previous
                    return grid
                case 3 :
                    grid[y_pose][x_pose] = previous
                    return(force_move(grid, (y_pose, x_pose - 1), direction, 3))
                case 4 :
                    grid[y_pose][x_pose] = previous
                    return(force_move(grid, (y_pose, x_pose - 1), direction, 4))
        
def move(grid, position, direction) :
    (y_pose, x_pose) = position
    match direction :
        case 0 :
            match grid[y_pose - 1][x_pose] :
                case 4 :
                    pushed, new_grid = push_box(grid, (y_pose - 1, x_pose - 1), (y_pose - 1, x_pose), direction)
                    if pushed :
                        new_grid[y_pose - 1][ x_pose] = 0
                        return(True, new_grid)
                    else :
                        return(False, grid)
                case 3 :
                    pushed, new_grid = push_box(grid, (y_pose - 1, x_pose), (y_pose - 1, x_pose + 1), direction)
                    if pushed :
                        new_grid[y_pose - 1][ x_pose] = 0
                        return(True, new_grid)
                    else :
                        return(False, grid)
                case 2 :
                    return (False, grid)
                case 0 :
                    return (True, grid)
        case 1 :
            match grid[y_pose][x_pose + 1] :
                case 3 :
                    pushed, new_grid = push_box(grid, (y_pose, x_pose + 1), (y_pose, x_pose + 2), direction)
                    if pushed :
                        new_grid[y_pose][ x_pose + 1] = 0
                        return(True, new_grid)
                    else :
                        return(False, grid)
                case 2 :
                    return (False, grid)
                case 0 :
                    return (True, grid)
        case 2 :
            match grid[y_pose + 1][x_pose] :
                case 4 :
                    pushed, new_grid = push_box(grid, (y_pose + 1, x_pose - 1), (y_pose + 1, x_pose), direction)
                    if pushed :
                        new_grid[y_pose + 1][ x_pose] = 0
                        return(True, new_grid)
                    else :
                        return(False, grid)
                case 3 :
                    pushed, new_grid = push_box(grid, (y_pose + 1, x_pose), (y_pose + 1, x_pose + 1), direction)
                    if pushed :
                        new_grid[y_pose + 1][ x_pose] = 0
                        return(True, new_grid)
                    else :
                        return(False, grid)
                case 2 :
                    return (False, grid)
                case 0 :
                    return (True, grid)
        case 3 :
            match grid[y_pose][x_pose - 1] :
                case 4 :
                    pushed, new_grid = push_box(grid, (y_pose, x_pose - 2), (y_pose, x_pose - 1), direction)
                    if pushed :
                        new_grid[y_pose][ x_pose - 1] = 0
                        return(True, new_grid)
                    else :
                        return(False, grid)
                case 2 :
                    return (False, grid)
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
        #print(direction)
        #print_grid(grid, (y_pose, x_pose))
        #input()
    return grid

def print_grid(grid, position) :
    (y_pose, x_pose) = position
    for y in range(len(grid)) :
        test = []
        for x in range(len(grid[y])) :
            if y == y_pose and x == x_pose :
                test.append('@')
            else :
                match grid[y][x] :
                    case 2 :
                        test.append('#')
                    case 1 :
                        print("probleme")
                    case 0 :
                        test.append(".")
                    case 3 :
                        test.append("[")
                    case 4 :
                        test.append("]")
        print("".join(test))
                    
def main() :
    textfile = get_input()
    grid, start_position, moves = get_grid(textfile)
    def_grid = compute_moves(grid, start_position, moves)
    sum = 0
    for y in range(len(def_grid)) :
        for x in range(len(def_grid[y])) :
            if def_grid[y][x] == 3 :
                sum += (100*y + x)
    print(sum)
    

if __name__=="__main__":
    main()