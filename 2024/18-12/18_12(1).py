import sys

def get_input() :
    return("example.txt")
    return("input.txt")

def get_grid(text) :
    with open(text) as file :
        data = file.read()
    bytes = data.split("\n")
    for i, byte in enumerate(bytes) :
        temp = byte.split(',')
        bytes[i] = (int(temp[1]), int(temp[0]))
    grid_width = 71
    grid_height = 71
    start_position = (0, 0)
    end_position = (70, 70)
    number_of_blocks = 1024
    i = 0
    grid = [[sys.maxsize for _ in range(grid_width)] for _ in range(grid_height)]
    while (i < len(bytes)) and (i < number_of_blocks) :
        y_block, x_block = bytes[i]
        grid[y_block][x_block] = -1
        i += 1
    grid[0][0] = 0
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
        if (y_pose != 0) and (grid[y_pose - 1][x_pose] != -1) and (grid[y_pose - 1][x_pose] > length + 1) :
            grid[y_pose - 1][x_pose] = length + 1
            queue.append(((y_pose-1, x_pose), length + 1))
        #right
        if (x_pose != len(grid[y_pose]) - 1) and (grid[y_pose][x_pose + 1] != -1) and (grid[y_pose][x_pose + 1] > length + 1) :
            grid[y_pose][x_pose + 1] = length + 1
            queue.append(((y_pose, x_pose+1), length + 1))
        #down
        if (y_pose != len(grid) - 1) and (grid[y_pose + 1][x_pose] != -1) and (grid[y_pose + 1][x_pose] > length + 1) :
            grid[y_pose + 1][x_pose] = length + 1
            queue.append(((y_pose+1, x_pose), length + 1))
        #left
        if (x_pose != 0) and (grid[y_pose][x_pose - 1] != -1) and (grid[y_pose][x_pose - 1] > length + 1) :
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
    grid, length = dijkstra(grid, start_position, end_position)
    print(length)

if __name__=="__main__":
    main()