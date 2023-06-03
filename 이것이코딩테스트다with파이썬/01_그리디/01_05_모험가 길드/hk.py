def solution(n,array):
    answer = 0

    array_sort = sorted(array)
    
    stack = 0
    for i in array_sort:
        stack += 1
        if stack >= i:
            answer += 1
            stack = 0
        # print(stack,i)

    
    return answer

# print(solution(5,[2,3,1,2,2,4,6,7]))