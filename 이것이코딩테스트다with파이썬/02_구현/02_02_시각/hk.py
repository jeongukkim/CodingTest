def solution(n):
    answer = 0

    three = [3,13,23,30,31,32,33,34,35,36,37,38,39,43,53]

    for t in range(n+1):
        if t in three:
            answer += 3600
        else:
            answer += (15*60) + (45*15)

    return answer

# print(solution(5))