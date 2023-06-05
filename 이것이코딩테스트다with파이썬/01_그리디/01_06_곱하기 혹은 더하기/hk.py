def solution(s):
    answer = int(s[0])

    for i in range(1,len(s)):
        temp = int(s[i])
        if answer == 0 or answer == 1:
            answer += temp
        else:
            if temp == 1 or temp == 0:
                answer += temp
            else:
                answer *= temp 

    return answer

print(solution("02984"))