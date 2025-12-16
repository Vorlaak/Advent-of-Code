def get_input():
    # return "example.txt"
    return "input.txt"


def get_locks_keys(text):
    locks, keys = [], []
    with open(text) as file:
        data = file.read().split("\n\n")
    for el in data:
        if el[0] == "#":
            locks.append(el)
        else:
            keys.append(el)
    return locks, keys


def process_locks(locks):
    new_locks = []
    for lock in locks:
        new_lock = [0 for _ in range(5)]
        rows = lock.split("\n")
        for row in rows:
            for i, el in enumerate(row):
                if el == "#":
                    new_lock[i] += 1
        new_locks.append(new_lock)
    return new_locks


def process_keys(keys):
    new_keys = []
    for key in keys:
        new_key = [0 for _ in range(5)]
        rows = key.split("\n")
        for row in rows:
            for i, el in enumerate(row):
                if el == "#":
                    new_key[i] += 1
        new_keys.append(new_key)
    return new_keys


def match_lock_key(lock, key):
    for i in range(5):
        if lock[i] + key[i] >= 8:
            return False
    return True


def main():
    textfile = get_input()
    locks, keys = get_locks_keys(textfile)
    locks, keys = process_locks(locks), process_keys(keys)
    counter = 0
    for lock in locks:
        for key in keys:
            if match_lock_key(lock, key):
                counter += 1
    print(counter)


if __name__ == "__main__":
    main()
