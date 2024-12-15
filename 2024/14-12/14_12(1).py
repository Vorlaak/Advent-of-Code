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
    steps = 100
    quad_1 = []
    quad_2 = []
    quad_3 = []
    quad_4 = []
    for robot in robots :
        [[pose_x, pose_y], [vel_x, vel_y]] = robot
        (x, y) = compute_robot((pose_x, pose_y), (vel_x, vel_y), steps, (grid_x, grid_y))
        if (x + 1) < ((grid_x + 1) / 2) and (y + 1) < ((grid_y + 1) / 2) :
            quad_1.append((x, y))
        elif (x + 1) > ((grid_x + 1) / 2) and (y + 1) < ((grid_y + 1) / 2) :
            quad_2.append((x, y))
        elif (x + 1) < ((grid_x + 1) / 2) and (y + 1) > ((grid_y + 1) / 2) :
            quad_3.append((x, y))
        elif (x + 1) > ((grid_x + 1) / 2) and (y + 1) > ((grid_y + 1) / 2) :
            quad_4.append((x, y))
    print(len(quad_1)*len(quad_2)*len(quad_3)*len(quad_4))
    
if __name__=="__main__":
    main()