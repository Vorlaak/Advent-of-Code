def get_input():
    # return "example.txt"
    return "input.txt"


def get_points(text):
    points = []
    with open(text) as file:
        for line in file:
            point = []
            for coord in line[:-1].split(","):
                point.append(int(coord))
            points.append(point)
    return points


def get_distances(points):
    distances = []
    for i in range(len(points) - 1):
        for j in range(i + 1, len(points)):
            distance = (
                (points[j][0] - points[i][0]) ** 2
                + (points[j][1] - points[i][1]) ** 2
                + (points[j][2] - points[i][2]) ** 2
            )
            distances.append([distance, i, j])
    return distances


def main():
    textfile = get_input()
    points = get_points(textfile)
    distances = get_distances(points)
    distances.sort(key=lambda x: x[0])
    groups = []
    for i in range(len(points)):
        groups.append({i})
    while len(groups) > 1:
        distance, i, j = distances.pop(0)
        flag = False
        for k, group in enumerate(groups):
            if i in group or j in group:
                if not flag:
                    flag = True
                    last = k
                    group.add(i)
                    group.add(j)
                else:
                    other_group = groups.pop(last)
                    for el in other_group:
                        group.add(el)

    print(points[i][0] * points[j][0])


if __name__ == "__main__":
    main()
