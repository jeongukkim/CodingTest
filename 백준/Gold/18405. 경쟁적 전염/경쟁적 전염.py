from collections import deque

n, k = map(int, input().split())

graph = []
data =[]

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] > 0:
            data.append((graph[i][j], 0, i, j))

data.sort()
queue = deque(data)

end_time, target_y, target_x = map(int, input().split())

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

while queue:
    virus_num, time, y, x = queue.popleft()
    if time == end_time: break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if not graph[ny][nx]:
                graph[ny][nx] = virus_num
                queue.append((virus_num, time+1, ny, nx))
                
print(graph[target_y-1][target_x-1])