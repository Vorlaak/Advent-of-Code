def get_input():
    # return "example.txt"
    return "input.txt"


def get_graph(text):
    graph = {}
    with open(text, "r") as f:
        for devices in [line.strip().split() for line in f]:
            graph[devices[0][:-1]] = devices[1:]
    return graph


def find_all_paths(graph, start, end, visited, scores):
    if start == end:
        return 1
    if start in visited or start == "out":
        return 0
    if start in scores:
        return scores[start]
    visited.add(start)
    total = sum(
        [find_all_paths(graph, output, end, visited, scores) for output in graph[start]]
    )
    visited.remove(start)
    scores[start] = total
    return total


def main():
    textfile = get_input()
    graph = get_graph(textfile)
    a1 = find_all_paths(graph, "svr", "fft", set(), {})
    a2 = find_all_paths(graph, "fft", "dac", set(), {})
    a3 = find_all_paths(graph, "dac", "out", set(), {})
    b1 = find_all_paths(graph, "svr", "dac", set(), {})
    b2 = find_all_paths(graph, "dac", "fft", set(), {})
    b3 = find_all_paths(graph, "fft", "out", set(), {})
    print(a1 * a2 * a3 + b1 * b2 * b3)


if __name__ == "__main__":
    main()
