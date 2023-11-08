def solution(n, times):
    answer = 0
    
    start = 0
    end = max(times) * n
    
    while start <= end:
        mid = (start + end) // 2
        
        num_person = 0
        for time in times:
            num_person += mid // time
        
        if num_person >= n:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
    
    return answer