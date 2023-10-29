def solution(plans):
    answer = []
    diff_m = 0
    
    plans.sort(key=lambda x: x[1])
    stack = []
    for i in range(len(plans)):
        now_name, now_time, now_runtime = plans[i]
        
        while stack:
            prev_name, prev_runtime = stack.pop()
            if diff_m >= prev_runtime:
                diff_m -= prev_runtime
                answer.append(prev_name)
            else :
                stack.append((prev_name, prev_runtime - diff_m))
                break
                
        stack.append((now_name, int(now_runtime)))
        
        if i < len(plans)-1 :
            now_h, now_m = list(map(int, now_time.split(":")))
            next_time = plans[i+1][1]
            next_h, next_m = list(map(int, next_time.split(":")))
            diff_m = next_m - now_m
            diff_h = next_h - now_h
            if diff_m < 0:
                diff_m += 60
                diff_h -= 1
            diff_m += diff_h * 60
    
    while stack:
        answer.append(stack.pop()[0])
        
    return answer
