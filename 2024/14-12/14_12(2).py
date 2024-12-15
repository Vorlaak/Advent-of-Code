import re

def get_input() :
    #return("example.txt")
    return("input.txt")

def get_robots(text) :
    pattern = r'[-+]?[.]?[\d]+(?:\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?'
    with open(text) as file :
        data = file.read()
    machines = data.split('\n')
    for i in range(len(machines)) :
        machines[i] = machines[i].split(' ')
        for j in range(len(machines[i])) :
            machines[i][j] = re.findall(pattern, machines[i][j])
            for k in range(len(machines[i][j])) :
                machines[i][j][k] = int(machines[i][j][k])
    return machines

def compute_robot(pose, vel, steps, grid) :
    new_pose_x = (pose[0] + (vel[0] * steps)) % grid[0]
    new_pose_y = (pose[1] + (vel[1] * steps)) % grid[1]
    return(new_pose_x, new_pose_y)
    

def main() :
    textfile = get_input()
    robots = get_robots(textfile)
    grid_x = 101
    grid_y = 103
    steps = 7037
    while True :
        print(steps)
        grid_image = [["."for _ in range(grid_x)] for _ in range(grid_y)]
        for robot in robots :
            [[pose_x, pose_y], [vel_x, vel_y]] = robot
            (x, y) = compute_robot((pose_x, pose_y), (vel_x, vel_y), steps, (grid_x, grid_y))
            grid_image[y][x] = "#"
        
        with open("grid.txt", "wt") as f :
            for line in grid_image :
                print("".join(line), file=f)
        steps += 10403
        input()
    
if __name__=="__main__":
    main()