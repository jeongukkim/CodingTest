def solution(n,m,k,array):
    answer = 0
    array_sort = sorted(array,reverse = True)
    a = array_sort[0]
    b = array_sort[1]

    stack = 0
    for i in range(m):
        if stack == k:
            answer += b
            stack = -1
        else:
            answer += a
        stack += 1
    
    return answer
print(solution(4, 6, 2, [1, 2, 3, 4]))