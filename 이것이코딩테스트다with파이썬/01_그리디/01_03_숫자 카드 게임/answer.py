def solution(n,m,array):

    result = 0
    # 한 줄씩 입력 받아 확인하기
    for i in range(n):
        # 현재 줄에서 '가장 작은 수' 찾기
        min_value = min(array[i])
        # '가장 작은 수'들 중에서 가장 큰 수 찾기
        result = max(result, min_value)
    
    return result

# print(solution(3, 3, [[3, 1, 2], [4, 1, 4], [2, 2, 2]]))