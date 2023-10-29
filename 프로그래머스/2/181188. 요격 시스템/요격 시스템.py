def solution(targets):
    answer = 0
    
    targets.sort(key=lambda x: x[1])
    prev_end = 0
    for now_start, now_end in targets:
        if now_start >= prev_end:
            prev_end = now_end
            answer += 1
    return answer