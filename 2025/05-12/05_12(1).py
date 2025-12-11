def get_input():
    # return "example.txt"
    return "input.txt"


def get_lists(text):
    with open(text) as file:
        data = file.read()
    ranges, ingredients = data.split("\n\n")[0], data.split("\n\n")[1]
    return ranges, ingredients


def process_ingredients(ranges):
    good_ingredients = []
    for ings in ranges:
        start, finish = ings.split("-")[0], ings.split("-")[1]
        new_range = [int(start), int(finish)]
        good_ingredients.append(new_range)
    return good_ingredients


def process_good(good_ingredients):
    merged = []
    good_ingredients.sort(key=lambda x: x[0])

    prev = good_ingredients[0]

    for interval in good_ingredients[1:]:
        if interval[0] <= prev[1]:
            prev[1] = max(prev[1], interval[1])
        else:
            merged.append(prev)
            prev = interval

    merged.append(prev)
    return merged


def main():
    textfile = get_input()
    ranges, ingredients = get_lists(textfile)
    ranges = ranges.split("\n")
    ingredients = ingredients.split("\n")[:-1]
    good_ingredients = process_ingredients(ranges=ranges)
    merged_good = process_good(good_ingredients=good_ingredients)
    counter = 0
    for ing in ingredients:
        for range in merged_good:
            if int(ing) <= range[1] and int(ing) >= range[0]:
                counter += 1
                break
    print(counter)


if __name__ == "__main__":
    main()
