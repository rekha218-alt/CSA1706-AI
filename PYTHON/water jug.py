from collections import deque

def water_jug():
    visited = set()
    queue = deque()

    queue.append((0, 0, []))

    while queue:
        a, b, path = queue.popleft()

        if (a, b) in visited:
            continue

        visited.add((a, b))
        path = path + [(a, b)]

        if a == 2:
            return path

        next_states = [
            (4, b),
            (a, 3),
            (0, b),
            (a, 0),
            (a - min(a, 3 - b), b + min(a, 3 - b)),
            (a + min(b, 4 - a), b - min(b, 4 - a))
        ]

        for state in next_states:
            if state not in visited:
                queue.append((state[0], state[1], path))

result = water_jug()

print("Steps:")

for step in result:
    print(step)
