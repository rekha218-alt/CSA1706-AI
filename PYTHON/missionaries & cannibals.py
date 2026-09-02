from collections import deque

start = (3, 3, 'L')
goal = (0, 0, 'R')

def is_valid(m, c):
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False
    if m > 0 and m < c:
        return False
    if (3 - m) > 0 and (3 - m) < (3 - c):
        return False
    return True

def next_states(state):
    m, c, side = state
    moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]
    states = []

    for dm, dc in moves:
        if side == 'L':
            nm = m - dm
            nc = c - dc
            ns = 'R'
        else:
            nm = m + dm
            nc = c + dc
            ns = 'L'

        if is_valid(nm, nc):
            states.append((nm, nc, ns))

    return states

def bfs():
    q = deque([(start,[start])])
    visited = set()

    while q:
        state, path = q.popleft()

        if state == goal:
            return path

        if state in visited:
            continue

        visited.add(state)

        for s in next_states(state):
            q.append((s, path+[s]))

solution = bfs()

print("Solution:")
for step in solution:
    print(step)
