def get_input():
    # return "example.txt"
    return "input.txt"


def get_lists(text, grid):
    with open(text) as file:
        for line in file:
            grid.append(list(line[:-1]))


def is_accessible(line, col, lines, cols, grid):
    counter = 0
    if line > 0 and col > 0:
        if grid[line - 1][col - 1] == "@":
            counter += 1
    if line > 0:
        if grid[line - 1][col] == "@":
            counter += 1
    if line > 0 and col < cols - 1:
        if grid[line - 1][col + 1] == "@":
            counter += 1
    if col > 0:
        if grid[line][col - 1] == "@":
            counter += 1
    if col < cols - 1:
        if grid[line][col + 1] == "@":
            counter += 1
    if line < lines - 1 and col > 0:
        if grid[line + 1][col - 1] == "@":
            counter += 1
    if line < lines - 1:
        if grid[line + 1][col] == "@":
            counter += 1
    if line < lines - 1 and col < cols - 1:
        if grid[line + 1][col + 1] == "@":
            counter += 1
    if counter < 4:
        grid[line][col] = "."
    return counter < 4


def process_grid(grid):
    lines = len(grid)
    cols = len(grid[0])
    counter = 0
    new_counter = 25
    while new_counter != 0:
        new_counter = 0
        for line in range(lines):
            for col in range(cols):
                if grid[line][col] == "@" and is_accessible(
                    line=line, col=col, lines=lines, cols=cols, grid=grid
                ):
                    new_counter += 1
                    counter += 1
    print(counter)


def main():
    textfile = get_input()
    grid = []
    get_lists(textfile, grid=grid)
    process_grid(grid=grid)


if __name__ == "__main__":
    main()
