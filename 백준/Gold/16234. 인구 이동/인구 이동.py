import sys
from collections import deque

input = sys.stdin.readline
n, min_val, max_val = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

answer = 0

def run(y, x, index):
    united = []
    united.append((y, x))
    queue = deque()
    queue.append((y, x))
    union[y][x] = index
    summary = graph[y][x]
    count = 1
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and union[ny][nx] == -1:
                if min_val <= abs(graph[ny][nx] - graph[y][x]) <= max_val:
                    queue.append((ny, nx))
                    union[ny][nx] = index
                    summary += graph[ny][nx]
                    count += 1
                    united.append((ny, nx))
    for y, x in united:
        graph[y][x] = int(summary / count)
    return count

total_count = 0

while True:
    union = [[-1] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                run(i, j, index)
                index += 1
    if index == n*n:
        break
    total_count += 1
    
print(total_count)
