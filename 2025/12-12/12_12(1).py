def get_input():
    # return "example.txt"
    return "input.txt"


def get_presents(lines):
    presents = []
    for group in lines:
        counter = 0
        rows = group.split("\n")[1:]
        for row in rows:
            for el in row:
                if el == "#":
                    counter += 1
        presents.append(counter)
    return presents


def get_spots(lines):
    rows = lines.split("\n")[:-1]
    spots = []
    for row in rows:
        size, presents = row.split(":")[0], row.split(":")[1].split()
        spots.append((size, presents))
    return spots


def get_presents_and_spots(text):
    with open(text) as file:
        lines = file.read().split("\n\n")
    presents = get_presents(lines[:-1])
    spots = get_spots(lines[-1])
    return presents, spots


def process_spot(spot, presents):
    width, length = int(spot[0].split("x")[0]), int(spot[0].split("x")[1])
    area = (width // 3) * (length // 3)
    counter = 0
    for i, present in enumerate(spot[1]):
        counter += int(present)
    return counter <= area


def main():
    textfile = get_input()
    presents, spots = get_presents_and_spots(textfile)
    counter = 0
    for spot in spots:
        if process_spot(spot, presents):
            counter += 1
    print(counter)


if __name__ == "__main__":
    main()
