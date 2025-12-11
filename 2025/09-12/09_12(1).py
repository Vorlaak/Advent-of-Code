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


def get_max_area(points):
    maxi = 0
    for i in range(len(points) - 1):
        for j in range(i + 1, len(points)):
            area = (abs(points[j][0] - points[i][0]) + 1) * (
                abs(points[j][1] - points[i][1]) + 1
            )
            maxi = max(maxi, area)
    return maxi


def main():
    textfile = get_input()
    points = get_points(textfile)
    print(get_max_area(points))


if __name__ == "__main__":
    main()
