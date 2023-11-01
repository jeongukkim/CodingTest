n = int(input())
data = list(map(int, input().split()))
plus, minus, pro, div = map(int, input().split())

min_val = 1e9
max_val = -1e9

def dfs(i, result):
    global min_val, max_val, plus, minus, pro, div
    if i == n:
        min_val = min(result, min_val) # min_val을 앞에 둘 시 float로 리턴함;;
        max_val = max(result, max_val)
    else:
        if plus > 0:
            plus -= 1
            dfs(i+1, result + data[i])
            plus += 1
        if minus > 0:
            minus -= 1
            dfs(i+1, result - data[i])
            minus += 1
        if pro > 0:
            pro -= 1
            dfs(i+1, result * data[i])
            pro += 1
        if div > 0:
            div -= 1
            dfs(i+1, int(result/data[i]))
            div += 1

dfs(1, data[0])

print(max_val)
print(min_val)
