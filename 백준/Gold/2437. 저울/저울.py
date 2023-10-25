n = int(input())
data = list(map(int, input().split()))
data.sort()

prefix_sum = 1
for value in data:
    if prefix_sum < value: break
    prefix_sum += value
print(prefix_sum)