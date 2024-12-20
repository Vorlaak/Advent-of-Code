import sys
from copy import deepcopy

def get_input() :
    #return("example.txt")
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
    position = start_position
    queue.append((position, 0))
    while len(queue) > 0 :
        index_min = find_min(queue)
        ((y_pose, x_pose), length) = queue.pop(index_min)
        if y_pose == end_position[0] and x_pose == end_position[1] :
            return(grid, length)
        #up
        if (grid[y_pose - 1][x_pose] != -1) and (grid[y_pose - 1][x_pose] > length + 1) :
            grid[y_pose - 1][x_pose] = length + 1
            queue.append(((y_pose-1, x_pose), length + 1))
        #right
        if (grid[y_pose][x_pose + 1] != -1) and (grid[y_pose][x_pose + 1] > length + 1) :
            grid[y_pose][x_pose + 1] = length + 1
            queue.append(((y_pose, x_pose+1), length + 1))
        #down
        if (grid[y_pose + 1][x_pose] != -1) and (grid[y_pose + 1][x_pose] > length + 1) :
            grid[y_pose + 1][x_pose] = length + 1
            queue.append(((y_pose+1, x_pose), length + 1))
        #left
        if (grid[y_pose][x_pose - 1] != -1) and (grid[y_pose][x_pose - 1] > length + 1) :
            grid[y_pose][x_pose - 1] = length + 1
            queue.append(((y_pose, x_pose-1), length + 1))
    return("unreachable")

def find_min(queue) :
    i = 0
    min_length = sys.maxsize
    count = 0
    for item in queue :
        if item[1] < min_length :
            i =  count
            min_length = item[1]
        count += 1
    return i

def main() :
    textfile = get_input()
    grid, start_position, end_position = get_grid(textfile)
    blank_grid = deepcopy(grid)
    grid, initial_length = dijkstra(grid, start_position, end_position)
    cheat_lengths = []
    for y in range(1, len(blank_grid) - 1) :
        for x in range(1, len(blank_grid[y]) - 1) :
            new_grid = deepcopy(blank_grid)
            if new_grid[y][x] == -1 :
                new_grid[y][x] = sys.maxsize
                new_grid, length = dijkstra(new_grid, start_position, end_position)
                if length < initial_length - 99 :
                    cheat_lengths.append(initial_length - length)
    print(len(cheat_lengths))

if __name__=="__main__":
    main()