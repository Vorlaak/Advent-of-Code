def get_input():
    # return "example.txt"
    return "input.txt"


def get_lines(text):
    lines = []
    with open(text) as file:
        for line in file:
            lines.append(line[:-1])
    return lines


def process_line(line, beams):
    new_beams = set()
    counter = 0
    for beam in beams:
        if line[beam] == ".":
            new_beams.add(beam)
        elif line[beam] == "^":
            counter += 1
            if beam > 0:
                new_beams.add(beam - 1)
            if beam < len(line) - 1:
                new_beams.add(beam + 1)
    return new_beams, counter


def main():
    textfile = get_input()
    lines = get_lines(textfile)
    beams = set()
    counter = 0
    for i, el in enumerate(lines[0]):
        if el == "S":
            beams.add(i)
    for i in range(1, len(lines)):
        new_beams, num = process_line(lines[i], beams)
        counter += num
        beams = new_beams
    print(counter)


if __name__ == "__main__":
    main()
