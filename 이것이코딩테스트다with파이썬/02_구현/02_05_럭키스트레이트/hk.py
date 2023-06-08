def solution(n):
    a = 0
    b = 0
    x = len(n)

    for i in range(x//2):
        a += int(n[i])

    for i in range(x//2,x):
        b += int(n[i])

    if a == b:
        return "LUCKY"
    else:
        return "READY"

# print(solution("123402"))