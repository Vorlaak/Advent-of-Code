from copy import deepcopy

def get_input() :
    return("example.txt")
    return("input.txt")

def get_codes(text) :
    with open(text) as file :
        data = file.read().split('\n')
    return(data)

def get_numerical() :
    grid = [[7, 8, 9], [4, 5, 6], [1, 2, 3], [-1, 0, 10]]
    return grid

def get_directional() :
    grid = [[-1, 0, 10], [3, 2, 1]]
    return grid            

def print_code(code) :
    ret = []
    for num in code :
        match num :
            case 10 :
                ret.append('A')
            case 0 :
                ret.append('^')
            case 1 :
                ret.append('>')
            case 2 :
                ret.append('v')
            case 3 :
                ret.append('<')
    print("".join(ret))

def decode(code, rob) :
    start = (0, 2)
    pad = get_directional()
    length = 0
    if rob == 0 :
        return len(code)
    for key in code :
        for y, row in enumerate(pad) :
            for x, but in enumerate(row) :
                if but == key :
                    end = (y, x)
        length += move(start, end, (0, 0), rob)
        start = end
    return length
        
def get_paths(start, end) :
    paths = [[start]]
    good_paths = []
    while len(paths) > 0 :
        path = paths.pop(0)
        new_start = path[-1]
        if new_start == end :
            good_paths.append(path)
        y_start, x_start = new_start
        if end[0] > y_start :
            paths.append(deepcopy(path)+[(y_start + 1, x_start)])
        if end[0] < y_start :
            paths.append(deepcopy(path)+[(y_start - 1, x_start)])
        if end[1] > x_start :
            paths.append(deepcopy(path)+[(y_start, x_start + 1)])
        if end[1] < x_start :
            paths.append(deepcopy(path)+[(y_start, x_start - 1)])
    return good_paths

def move(start, end, forbi, rob) :
    (y_start, x_start) = start
    (y_end, x_end) = end
    (y_forbi, x_forbi) = forbi
    paths = get_paths(start, end)
    good_paths = []
    for path in paths :
        if forbi not in path :
            good_paths.append(path)
    codes = [code(path) for path in good_paths]
    return min([decode(x, rob - 1) for x in codes])

def code(path) :
    y_cursor, x_cursor = path[0][0], path[0][1]
    code = []
    for i in range(1, len(path)) :
        y_pose, x_pose = path[i]
        if y_pose < y_cursor :
            y_cursor = y_pose
            code.append(0)
        elif x_pose > x_cursor :
            x_cursor = x_pose
            code.append(1)
        elif y_pose > y_cursor :
            y_cursor = y_pose
            code.append(2)
        elif x_pose < x_cursor :
            x_cursor = x_pose
            code.append(3)
    code.append(10)
    return code

def main() :
    textfile = get_input()
    codes = get_codes(textfile)
    numpad = get_numerical()
    sum = 0
    for code in codes :
        length = 0
        start = (3, 2)
        for key in code :
            if key == 'A' :
                num = 10
            else :
                num = int(key)
            for y, row in enumerate(numpad) :
                for x, but in enumerate(row) :
                    if but == num :
                        end = (y, x)
            length += move(start, end, (3, 0), 3)
            start = end
        sum += int(code[:-1]) * length
    print(sum)

if __name__=="__main__":
    main()