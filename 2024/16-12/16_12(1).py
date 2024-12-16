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
    for i in range(len(maze)) :
        line_list = []
        for j in range(len(maze[i])) :
            if maze[i][j] == "#" :
                line_list.append(-1)
            elif maze[i][j] == "." :
                line_list.append(sys.maxsize)
            elif maze[i][j] == "S" :
                start_position = (i, j)
                line_list.append(0)
            elif maze[i][j] == "E" :
                end_position = (i, j)
                line_list.append(sys.maxsize)
        grid.append(line_list)
    return grid, start_position, end_position

def dijkstra(grid, start_position, end_position) :
    queue = []
    direction = 1
    position = start_position
    queue.append((position, direction, 0))
    while len(queue) > 0 :
        index_min = find_min(queue)
        ((y_pose, x_pose), direc, length) = queue.pop(index_min)
        if y_pose == end_position[0] and x_pose == end_position[1] :
            return(grid, length)
        #up
        if direc == 0 :
            if (grid[y_pose - 1][x_pose] != -1) and (grid[y_pose - 1][x_pose] > length + 1) :
                grid[y_pose - 1][x_pose] = length + 1
                queue.append(((y_pose-1, x_pose), direc, length + 1))
        else :
            if (grid[y_pose - 1][x_pose] != -1) and (grid[y_pose - 1][x_pose] > length + 1001) :
                grid[y_pose - 1][x_pose] = length + 1001
                queue.append(((y_pose-1, x_pose), 0, length + 1001))
        #right
        if direc == 1 :
            if (grid[y_pose][x_pose + 1] != -1) and (grid[y_pose][x_pose + 1] > length + 1) :
                grid[y_pose][x_pose + 1] = length + 1
                queue.append(((y_pose, x_pose+1), direc, length + 1))
        else :
            if (grid[y_pose][x_pose + 1] != -1) and (grid[y_pose][x_pose + 1] > length + 1001) :
                grid[y_pose][x_pose + 1] = length + 1001
                queue.append(((y_pose, x_pose+1), 1, length + 1001))
        #down
        if direc == 2 :
            if (grid[y_pose + 1][x_pose] != -1) and (grid[y_pose + 1][x_pose] > length + 1) :
                grid[y_pose + 1][x_pose] = length + 1
                queue.append(((y_pose+1, x_pose), direc, length + 1))
        else :
            if (grid[y_pose + 1][x_pose] != -1) and (grid[y_pose + 1][x_pose] > length + 1001) :
                grid[y_pose + 1][x_pose] = length + 1001
                queue.append(((y_pose+1, x_pose), 2, length + 1001))
        #left
        if direc == 3 :
            if (grid[y_pose][x_pose - 1] != -1) and (grid[y_pose][x_pose - 1] > length + 1) :
                grid[y_pose][x_pose - 1] = length + 1
                queue.append(((y_pose, x_pose-1), direc, length + 1))
        else :
            if (grid[y_pose][x_pose - 1] != -1) and (grid[y_pose][x_pose - 1] > length + 1001) :
                grid[y_pose][x_pose - 1] = length + 1001
                queue.append(((y_pose, x_pose-1), 3, length + 1001))
    return("unreachable")

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

def main() :
    textfile = get_input()
    grid, start_position, end_position = get_grid(textfile)
    grid, length = dijkstra(grid, start_position, end_position)
    #for line in grid :
        #print(line)
    print(length)
if __name__=="__main__":
    main()