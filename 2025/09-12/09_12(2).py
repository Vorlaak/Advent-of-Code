def get_input():
    # return "example.txt"
    return "input.txt"


def get_points(text):
    points = []
    with open(text) as file:
        data = file.read()
        for line in data.splitlines():
            coords = line.split(",")
            points.append((int(coords[0]), int(coords[1])))
    return points


def get_area(x1, y1, x2, y2):
    x = abs(x1 - x2) + 1
    y = abs(y1 - y2) + 1
    return x * y


def process_points(points):
    n = len(points)
    edges = []
    sizes = []
    for i in range(n):
        edges.append(sorted((points[i], points[i - 1])))
        for j in range(i + 1, n):
            c1, c2 = sorted((points[i], points[j]))
            sizes.append((get_area(*c1, *c2), c1, c2))

    edges.sort(reverse=True, key=lambda e: get_area(*e[0], *e[1]))
    sizes.sort(reverse=True)

    for size, (x1, y1), (x2, y2) in sizes:
        y1, y2 = sorted((y1, y2))
        if not any(
            (x4 > x1 and x3 < x2 and y4 > y1 and y3 < y2)
            for (x3, y3), (x4, y4) in edges
        ):
            return size


def main():
    textfile = get_input()
    points = get_points(textfile)
    size = process_points(points)
    print(size)


if __name__ == "__main__":
    main()
