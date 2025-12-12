from z3 import IntVector, Optimize, Int


def get_input():
    # return "example.txt"
    return "input.txt"


def get_machines(text):
    data = []
    with open(text) as file:
        lines = file.read().splitlines()
    for line in lines:
        machine = {}
        tokens = line.split()

        buttons = [
            tuple(int(x) for x in token[1:-1].split(",")) for token in tokens[1:-1]
        ]
        machine["buttons"] = buttons

        joltage = tuple(int(x) for x in tokens[-1][1:-1].split(","))
        machine["joltage"] = joltage
        data.append(machine)
    return data


def process_machine(machine):
    buttons = machine["buttons"]
    joltage = machine["joltage"]

    counters = [[] for _ in range(len(joltage))]

    for b, button in enumerate(buttons):
        for c in button:
            counters[c].append(b)

    btn = IntVector("btn", len(buttons))
    presses = Int("presses")

    s = Optimize()
    for c in range(len(counters)):
        s.add(sum(btn[b] for b in counters[c]) == joltage[c])

    for b in range(len(buttons)):
        s.add(btn[b] >= 0)

    s.add(sum(btn) == presses)
    s.minimize(presses)
    s.check()
    m = s.model()

    presses = m.eval(presses).as_long()

    return presses


def process_machines(machines):
    total_presses = 0
    for machine in machines:
        presses = process_machine(machine)
        total_presses += presses
    return total_presses


def main():
    textfile = get_input()
    machines = get_machines(textfile)
    presses = process_machines(machines)
    print()
    print("Button presses:", presses)


if __name__ == "__main__":
    main()
