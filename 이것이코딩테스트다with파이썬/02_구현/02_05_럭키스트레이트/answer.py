def solution(n):
    answer = ""
    length = len(n) # 점수 값의 총 자릿수
    summary = 0
    for i in range(length // 2):
        summary += int(n[i])

    # 오른쪽 부분의 자릿수의 합 빼기
    for i in range(length // 2, length):
        summary -= int(n[i])

    # 왼쪽 부분과 오른쪽 부분의 자릿수 합이 동일한지 검사
    if summary == 0:
        answer = "LUCKY"
    else:
        answer = "READY"

    return answer

# print(solution("123402"))