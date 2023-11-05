import heapq

n = int(input())

data = []
for _ in range(n):
    heapq.heappush(data, int(input()))

result = 0
while len(data) > 1:
    one = heapq.heappop(data)
    two = heapq.heappop(data)
    sum_val = one + two
    result += sum_val
    heapq.heappush(data, sum_val)

print(result)
