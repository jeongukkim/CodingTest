def solution(n):
    answer = 0
    
    dic = {}

    for yy in range(1,9):
        for xx in range(1,9):
            dic[(xx,yy)] = 1

    x = ord(n[0])-96
    y = int(n[1])

    li = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

    for xx,yy in li:
        if dic.get((x+xx,y+yy)):
            answer += 1

    return answer

print(solution("a1"))