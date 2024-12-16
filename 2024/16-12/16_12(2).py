import sys

def get_input() :
    return("example.txt")
    return("input.txt")

def get_grid(text) :
    with open(text) as file :
        data = file.read()
    maze = data.split("\n")
    start_position = (0, 0)
    end_position = (0, 0)
    grid = []
    empty = []
    for i in range(len(maze)) :
        line_list = []
        empty_list = []
        for j in range(len(maze[i])) :
            if maze[i][j] == "#" :
                line_list.append([-1])
                empty_list.append([-1])
            elif maze[i][j] == "." :
                line_list.append([[sys.maxsize],[sys.maxsize],[sys.maxsize],[sys.maxsize]])
                empty_list.append(False)
            elif maze[i][j] == "S" :
                start_position = (i, j)
                line_list.append([[sys.maxsize],[0],[sys.maxsize],[sys.maxsize]])
                empty_list.append(False)
            elif maze[i][j] == "E" :
                end_position = (i, j)
                line_list.append([[sys.maxsize],[sys.maxsize],[sys.maxsize],[sys.maxsize]])
                empty_list.append(True)
        grid.append(line_list)
        empty.append(empty_list)
    return grid, start_position, end_position, empty

def dijkstra(grid, start_position, end_position) :
    queue = []
    direction = 1
    position = start_position
    queue.append((position, direction, 0))
    best_paths = []
    while len(queue) > 0 :
        index_min = find_min(queue)
        ((y_pose, x_pose), direc, length) = queue.pop(index_min)
        if y_pose == end_position[0] and x_pose == end_position[1] :
            if (len(best_paths) == 0) :
                best_paths.append(length)
                best_paths.append(direc)
            elif best_paths[0] == length :
                if direc not in best_paths :
                    best_paths.append(direc)
        #up
        if direc == 0 :
            if (len(grid[y_pose - 1][x_pose]) != 1) and (grid[y_pose - 1][x_pose][0][0] > length + 1) :
                grid[y_pose - 1][x_pose][0] = [length + 1, direc]
                queue.append(((y_pose-1, x_pose), direc, length + 1))
            elif (len(grid[y_pose - 1][x_pose]) != 1) and (grid[y_pose - 1][x_pose][0][0] == length + 1) :
                if direc not in grid[y_pose - 1][x_pose][0] :
                    grid[y_pose - 1][x_pose][0].append(direc)
                queue.append(((y_pose-1, x_pose), direc, length + 1))
        else :
            if grid[y_pose][x_pose][0][0] > length + 1000 :
                grid[y_pose][x_pose][0] = [length + 1000, direc]
                queue.append(((y_pose, x_pose), 0, length + 1000))
            if grid[y_pose][x_pose][0][0] == length + 1000 :
                if direc not in grid[y_pose][x_pose][0] :
                    grid[y_pose][x_pose][0].append(direc)
                queue.append(((y_pose, x_pose), 0, length + 1000))
        #right
        if direc == 1 :
            if (len(grid[y_pose][x_pose + 1]) != 1) and (grid[y_pose][x_pose + 1][1][0] > length + 1) :
                grid[y_pose][x_pose + 1][1] = [length + 1, direc]
                queue.append(((y_pose, x_pose+1), direc, length + 1))
            elif (len(grid[y_pose][x_pose + 1]) != 1) and (grid[y_pose][x_pose + 1][1][0] == length + 1) :
                if direc not in grid[y_pose][x_pose + 1][1] :
                    grid[y_pose][x_pose + 1][1].append(direc)
                queue.append(((y_pose, x_pose+1), direc, length + 1))
        else :
            if grid[y_pose][x_pose][1][0] > length + 1000 :
                grid[y_pose][x_pose][1] = [length + 1000, direc]
                queue.append(((y_pose, x_pose), 1, length + 1000))
            elif grid[y_pose][x_pose][1][0] == length + 1000 :
                if direc not in grid[y_pose][x_pose][1] :
                    grid[y_pose][x_pose][1].append(direc)
                queue.append(((y_pose, x_pose), 1, length + 1000))
        #down
        if direc == 2 :
            if (len(grid[y_pose + 1][x_pose]) != 1) and (grid[y_pose + 1][x_pose][2][0] > length + 1) :
                grid[y_pose + 1][x_pose][2] = [length + 1, direc]
                queue.append(((y_pose+1, x_pose), direc, length + 1))
            elif (len(grid[y_pose + 1][x_pose]) != 1) and (grid[y_pose + 1][x_pose][2][0] == length + 1) :
                if direc not in grid[y_pose + 1][x_pose][2] :
                    grid[y_pose + 1][x_pose][2].append(direc)
                queue.append(((y_pose+1, x_pose), direc, length + 1))
        else :
            if grid[y_pose][x_pose][2][0] > length + 1000 :
                grid[y_pose][x_pose][2] = [length + 1000, direc]
                queue.append(((y_pose, x_pose), 2, length + 1000))
            elif grid[y_pose][x_pose][2][0] == length + 1000 :
                if direc not in grid[y_pose][x_pose][2] :
                    grid[y_pose][x_pose][2].append(direc)
                queue.append(((y_pose, x_pose), 2, length + 1000))
        #left
        if direc == 3 :
            if (len(grid[y_pose][x_pose - 1]) != 1) and (grid[y_pose][x_pose - 1][3][0] > length + 1) :
                grid[y_pose][x_pose - 1][3] = [length + 1, direc]
                queue.append(((y_pose, x_pose-1), direc, length + 1))
            elif (len(grid[y_pose][x_pose - 1]) != 1) and (grid[y_pose][x_pose - 1][3][0] == length + 1) :
                if direc not in grid[y_pose][x_pose - 1][3] :
                    grid[y_pose][x_pose - 1][3].append(direc)
                queue.append(((y_pose, x_pose-1), direc, length + 1))
        else :
            if grid[y_pose][x_pose][3][0] > length + 1000 :
                grid[y_pose][x_pose][3] = [length + 1000, direc]
                queue.append(((y_pose, x_pose), 3, length + 1000))
            elif grid[y_pose][x_pose][3][0] == length + 1000 :
                if direc not in grid[y_pose][x_pose][3] :
                    grid[y_pose][x_pose][3].append(direc)
                queue.append(((y_pose, x_pose), direc, length + 1000))
    return(grid, best_paths)

def find_min(queue) :
    i = 0
    min_length = sys.maxsize
    count = 0
    for item in queue :
        if item[2] < min_length :
            i =  count
            min_length = item[2]
        count += 1
    return i

def get_paths(grid, empty, end_position, directions) :
    poses = [end_position]
    direcs = [directions]
    while len(poses) > 0 :
        pose = poses.pop(0)
        directs = direcs.pop(0)
        for dire in directs :
            match dire :
                case 0 :
                    data = grid[pose[0]][pose[1]][0]
                    for new_dir in data[1:] :
                        if new_dir == 0 :
                            poses.append((pose[0]+1,pose[1]))
                            direcs.append([0])
                            empty[pose[0]+1][pose[1]] = True
                        else :
                            poses.append(pose)
                            direcs.append([new_dir])
                case 1 :
                    data = grid[pose[0]][pose[1]][1]
                    for new_dir in data[1:] :
                        if new_dir == 1 :
                            poses.append((pose[0],pose[1]-1))
                            direcs.append([1])
                            empty[pose[0]][pose[1]-1] = True
                        else :
                            poses.append(pose)
                            direcs.append([new_dir])
                case 2 :
                    data = grid[pose[0]][pose[1]][2]
                    for new_dir in data[1:] :
                        if new_dir == 2 :
                            poses.append((pose[0]-1,pose[1]))
                            direcs.append([2])
                            empty[pose[0]-1][pose[1]] = True
                        else :
                            poses.append(pose)
                            direcs.append([new_dir])
                case 3 :
                    data = grid[pose[0]][pose[1]][3]
                    for new_dir in data[1:] :
                        if new_dir == 3 :
                            poses.append((pose[0],pose[1]+1))
                            direcs.append([3])
                            empty[pose[0]][pose[1]+1] = True
                        else :
                            poses.append(pose)
                            direcs.append([new_dir])
    count = 0
    for y in range(len(empty)) :
        for x in range(len(empty[y])) :
            if empty[y][x] == True:
                count += 1
    return (count, empty)

def main() :
    textfile = get_input()
    grid, start_position, end_position, empty = get_grid(textfile)
    grid, best_paths = dijkstra(grid, start_position, end_position)
    #for line in grid :
        #print(line)
    sum, empty = get_paths(grid, empty, end_position, best_paths[1:])
    print(sum)
    #for line in empty :
        #print(line)
    #for line in grid :
        #print(line)

if __name__=="__main__":
    main()