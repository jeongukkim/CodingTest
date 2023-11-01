import sys
from itertools import combinations

input = sys.stdin.readline
n, m = map(int, input().split())
chicken, house = [], []

for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append((r, c))
        elif data[c] == 2:
            chicken.append((r, c))

candidates = list(combinations(chicken, m))

def get_sum(candidate):
    result = 0
    for hy, hx in house:
        temp = 1e9
        for cy, cx in candidate:
            temp = min(temp, abs(hx-cx) + abs(hy-cy))
        result += temp
    return result

result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))

print(result)