def solution(distance, rocks, n):
    answer = 0
    
    rocks.sort()
    rocks.append(distance)
    
    start = 0
    end = distance
    
    while start <= end:
        mid = (start + end) // 2
        
        num_removed_rocks = 0
        value = 0
        for rock in rocks:
            if rock < value + mid:
                num_removed_rocks += 1
            else:
                value = rock
        
        if num_removed_rocks <= n:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1

    return answer