def solution(n,k):
    answer = 0
    
    if n == 1:
        return 0

    while n != 1:
        
        if n%k == 0:
            n = n//k
        else:
            n -= 1

        answer += 1
    return answer

# print(solution(100,3))