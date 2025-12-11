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
    new_beams = {}
    for beam in beams.keys():
        if line[beam] == ".":
            new_beams[beam] = new_beams.get(beam, 0) + beams.get(beam)
        elif line[beam] == "^":
            if beam > 0:
                new_beams[beam - 1] = new_beams.get(beam - 1, 0) + beams.get(beam)
            if beam < len(line) - 1:
                new_beams[beam + 1] = new_beams.get(beam + 1, 0) + beams.get(beam)
    return new_beams


def main():
    textfile = get_input()
    lines = get_lines(textfile)
    beams = {}
    counter = 0
    for i, el in enumerate(lines[0]):
        if el == "S":
            beams[i] = beams.get(i, 0) + 1
    for i in range(1, len(lines)):
        new_beams = process_line(lines[i], beams)
        beams = new_beams
    for i, val in beams.items():
        counter += val
    print(counter)


if __name__ == "__main__":
    main()
