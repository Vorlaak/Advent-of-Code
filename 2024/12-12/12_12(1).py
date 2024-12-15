def get_input() :
    #return("example.txt")
    return("input.txt")

def get_grid(text) :
    with open(text) as file :
        grid = []
        checked = []
        for linestring in file :
            line = []
            checked_line = []
            for char in linestring :
                line.append(char)
                checked_line.append(False)
            grid.append(line[:-1])
            checked.append(checked_line[:-1])
    return grid, checked

def check_group(poses, grid) :
    sum = 0
    for pose in poses :
        (y, x) = pose
        price = 0
        #left
        if (x == 0) or ((y, x-1) not in poses) :
            price += 1
        #up
        if (y == 0) or ((y-1, x) not in poses):
            price += 1
        #right
        if (x == (len(grid[y]) - 1)) or ((y, x+1) not in poses):
            price += 1
        #down
        if (y == (len(grid) - 1)) or ((y+1, x) not in poses):
            price += 1
        sum += price
    return (sum * len(poses))

def create_groups(grid, checked) :
    groups = []
    for y in range(len(grid)) :
        for x in range(len(grid[y])) :
            if not checked[y][x] :
                group = []
                to_check = [(y, x)]
                while len(to_check) > 0 :
                    (y_pose, x_pose) = to_check.pop(0)
                    checked[y_pose][x_pose] = True
                    if (y_pose, x_pose) not in group :
                        group.append((y_pose, x_pose))
                    if (y_pose != 0) and (not checked[y_pose-1][x_pose]) and (grid[y_pose-1][x_pose] == grid[y_pose][x_pose]) :
                        checked[y_pose-1][x_pose] = True
                        to_check.append((y_pose-1, x_pose))
                    if (x_pose != 0) and (not checked[y_pose][x_pose-1]) and (grid[y_pose][x_pose-1] == grid[y_pose][x_pose]) :
                        checked[y_pose][x_pose-1] = True
                        to_check.append((y_pose, x_pose-1))
                    if (y_pose != len(grid)-1) and (not checked[y_pose+1][x_pose]) and (grid[y_pose+1][x_pose] == grid[y_pose][x_pose]) :
                        checked[y_pose+1][x_pose] = True
                        to_check.append((y_pose+1, x_pose))
                    if (x_pose != len(grid[y_pose])-1) and (not checked[y_pose][x_pose+1]) and (grid[y_pose][x_pose+1] == grid[y_pose][x_pose]) :
                        checked[y_pose][x_pose+1]
                        to_check.append((y_pose, x_pose+1))
                groups.append(group)
    return groups
                        
def main() :
    textfile = get_input()
    grid, checked = get_grid(textfile)
    groups = create_groups(grid, checked)
    big_sum = 0
    for group in groups :
        big_sum += check_group(group, grid)
    print(big_sum)

if __name__=="__main__":
    main()