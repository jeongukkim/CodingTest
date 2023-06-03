def solution(n,m,array):
    answer = -1

    for i in array:
        answer = max(answer,min(i))
    
    return answer

# print(solution(3, 3, [[3, 1, 2], [4, 1, 4], [2, 2, 2]]))