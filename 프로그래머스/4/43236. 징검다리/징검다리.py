INF = 1e9


def solution(distance, rocks, n):
    answer = 0
    
    rocks.sort()
    rocks.append(distance)
    
    start = 0
    end = distance
    
    while start <= end:
        mid = (start + end) // 2
        
        min_distance = int(INF)
        num_removed_rocks = 0
        value = 0
        for rock in rocks:
            if rock < value + mid:
                num_removed_rocks += 1
            else:
                min_distance = min(min_distance, rock - value)
                value = rock
        
        if num_removed_rocks <= n:
            answer = min_distance
            start = mid + 1
        else:
            end = mid - 1

    return answer