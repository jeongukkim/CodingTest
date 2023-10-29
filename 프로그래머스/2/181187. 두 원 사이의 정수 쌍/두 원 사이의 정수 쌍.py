from math import ceil

def solution(r1, r2):
    answer = 0
    for i in range(1, r2+1):
        answer += int((r2 ** 2 - i ** 2) ** 0.5) + 1
        if r1 >= i:
            answer -= ceil((r1 ** 2 - i ** 2) ** 0.5)
    answer *= 4
    return answer