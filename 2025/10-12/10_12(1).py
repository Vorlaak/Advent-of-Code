from itertools import combinations


def get_input():
    # return "example.txt"
    return "input.txt"


def get_machines(text):
    data = []
    with open(text) as file:
        lines = file.read().split("\n")
        for line in lines:
            data.append(line.split(" "))
    return data


def get_light_pattern(lights):
    pattern = []
    for light in lights[1:-1]:
        if light == ".":
            pattern.append(0)
        elif light == "#":
            pattern.append(1)
        else:
            print("PROBLEM")
    return pattern


def get_all_combinations(buttons):
    res = [list(combinations(buttons, r)) for r in range(1, len(buttons) + 1)]
    res = [list(sublist) for g in res for sublist in g]
    return res


def get_button_pattern(buttons, size):
    lights = [0 for _ in range(size)]
    for button in buttons:
        toggles = button[1:-1].split(",")
        for toggle in toggles:
            change = int(toggle)
            if lights[change] == 0:
                lights[change] = 1
            elif lights[change] == 1:
                lights[change] = 0
            else:
                print("OTHER PROBLEM")
    return lights


def process_machine(machine):
    lights, buttons, joltages = machine[0], machine[1:-1], machine[-1]
    pattern = get_light_pattern(lights)
    combos = get_all_combinations(buttons)
    size = len(pattern)
    for combo in combos:
        if get_button_pattern(combo, size) == pattern:
            return len(combo)


def main():
    textfile = get_input()
    machines = get_machines(textfile)[:-1]
    counter = 0
    for machine in machines:
        counter += process_machine(machine)
    print(counter)


if __name__ == "__main__":
    main()
