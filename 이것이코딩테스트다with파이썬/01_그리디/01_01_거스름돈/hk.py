def solution(a):
    answer = 0
    li = [500,100,50,10]
    for l in li:
        while a >= l:
            answer += 1
            a -= l
    print(a)
    return answer

print(solution(990))