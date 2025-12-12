from functools import lru_cache


def get_input():
    # return "example.txt"
    return "input.txt"


def get_devices(text):
    data = []
    with open(text) as file:
        lines = file.read().splitlines()
    for line in lines:
        device = {}
        tokens = line.split(":")
        name = tokens[0]
        outputs = tokens[1].split()
        device["name"] = name
        device["outputs"] = outputs
        data.append(device)
    return data


@lru_cache(maxsize=None)
def count_inputs(device):
    counter = 0
    for new_device in devices:
        if device in new_device["outputs"]:
            if new_device["name"] == "you":
                return 1
            counter += count_inputs(new_device["name"])
    return counter


def main():
    textfile = get_input()
    global devices
    devices = get_devices(textfile)[:-1]
    print(count_inputs("out"))


if __name__ == "__main__":
    main()
