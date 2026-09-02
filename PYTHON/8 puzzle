from collections import deque

goal = ((1,2,3),
        (4,5,6),
        (7,8,0))

def get_next(state):
    board = [list(row) for row in state]

    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                x, y = i, j

    moves = [(-1,0),(1,0),(0,-1),(0,1)]
    next_states = []

    for dx, dy in moves:
        nx, ny = x + dx, y + dy

        if 0 <= nx < 3 and 0 <= ny < 3:
            temp = [row[:] for row in board]
            temp[x][y], temp[nx][ny] = temp[nx][ny], temp[x][y]
            next_states.append(tuple(tuple(r) for r in temp))

    return next_states

def solve(start):
    q = deque()
    q.append((start,[start]))

    visited = set()

    while q:
        state, path = q.popleft()

        if state == goal:
            return path

        if state in visited:
            continue

        visited.add(state)

        for nxt in get_next(state):
            if nxt not in visited:
                q.append((nxt, path+[nxt]))

    return None

print("Enter Initial State")

start = []

for i in range(3):
    row = list(map(int, input().split()))
    start.append(tuple(row))

start = tuple(start)

answer = solve(start)

if answer:
    for i, state in enumerate(answer):
        print("\nStep", i)
        for row in state:
            print(*row)
else:
    print("No Solution")
