def solution(n,m,k,array):
    array.sort() # 입력 받은 수들 정렬하기
    first = array[n - 1] # 가장 큰 수
    second = array[n - 2] # 두 번째로 큰 수

    # 가장 큰 수가 더해지는 횟수 계산
    count = int(m / (k + 1)) * k
    count += m % (k + 1)

    result = 0
    result += (count) * first # 가장 큰 수 더하기
    result += (m - count) * second # 두 번째로 큰 수 더하기

    return result

print(solution(5, 8, 3, [2, 4, 5, 4, 6]))