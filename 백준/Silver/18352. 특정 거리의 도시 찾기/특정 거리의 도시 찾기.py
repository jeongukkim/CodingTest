import sys
from collections import deque

input = sys.stdin.readline
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [-1] * (n+1)

# BFS
queue = deque()
queue.append(x)
distance[x] = 0

answer = []
while queue:
    now = queue.popleft()    
    for next in graph[now]:
        if distance[next] == -1:
            distance[next] = distance[now] + 1
            queue.append(next)

check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True

if not check:
    print(-1)