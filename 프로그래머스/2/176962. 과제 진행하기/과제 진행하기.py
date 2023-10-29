def solution(plans):
    answer = []
    
    plans.sort(key=lambda x: x[1])
    stack = []
    for plan in plans:
        if not stack:
            stack.append(plan)
            continue
        prev_plan = stack.pop()
        prev_h, prev_m = list(map(int, prev_plan[1].split(":")))
        now_h, now_m = list(map(int, plan[1].split(":")))
        diff_m = now_m - prev_m
        diff_h = now_h - prev_h
        if diff_m < 0:
            diff_m += 60
            diff_h -= 1
        diff_m += diff_h * 60
        
        if int(prev_plan[2]) > diff_m:
            prev_plan[2] = f"{int(prev_plan[2]) - diff_m}"
            stack.append(prev_plan)
        else:
            answer.append(prev_plan[0])
            while stack:
                diff_m = diff_m - int(prev_plan[2])
                prev_plan = stack.pop()
                if int(prev_plan[2]) > diff_m:
                    prev_plan[2] = f"{int(prev_plan[2]) - diff_m}"
                    stack.append(prev_plan)
                    break
                else:
                    answer.append(prev_plan[0])
        stack.append(plan)
    
    while stack:
        answer.append(stack.pop()[0])
        
    
    return answer