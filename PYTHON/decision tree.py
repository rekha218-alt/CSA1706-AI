# Simple Decision Tree using ID3

from math import log2

data = [
    ["Sunny", "Hot", "No"],
    ["Sunny", "Cool", "Yes"],
    ["Rainy", "Cool", "Yes"],
    ["Rainy", "Hot", "No"],
    ["Cloudy", "Hot", "Yes"]
]

attributes = ["Weather", "Temperature"]


def entropy(rows):
    count = {}

    for row in rows:
        target = row[-1]
        count[target] = count.get(target, 0) + 1

    total = len(rows)
    result = 0

    for value in count.values():
        p = value / total
        result -= p * log2(p)

    return result


def information_gain(rows, index):
    total_entropy = entropy(rows)
    values = set(row[index] for row in rows)

    weighted_entropy = 0

    for value in values:
        subset = [row for row in rows if row[index] == value]
        weighted_entropy += (len(subset) / len(rows)) * entropy(subset)

    return total_entropy - weighted_entropy


def build_tree(rows, attrs):

    classes = [row[-1] for row in rows]

    if classes.count(classes[0]) == len(classes):
        return classes[0]

    if len(attrs) == 0:
        return max(set(classes), key=classes.count)

    gains = [information_gain(rows, i) for i in range(len(attrs))]
    best_index = gains.index(max(gains))
    best_attribute = attrs[best_index]

    tree = {best_attribute: {}}

    values = set(row[best_index] for row in rows)

    for value in values:
        subset = [row for row in rows if row[best_index] == value]

        new_rows = []
        for row in subset:
            new_row = row[:best_index] + row[best_index + 1:]
            new_rows.append(new_row)

        new_attrs = attrs[:best_index] + attrs[best_index + 1:]

        tree[best_attribute][value] = build_tree(
            new_rows, new_attrs
        )

    return tree


tree = build_tree(data, attributes)

print("Decision Tree:")
print(tree)
