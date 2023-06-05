def solution(food_times,k):

    if sum(food_times) <= k:
        return -1
    
    stack = 0
    start_end = 0
    while True:
        if food_times[stack] == 0:
            ## 리스트의 0으로 한바퀴 돌았다면
            start_end += 1
            if start_end == len(food_times):
                return -1

        else:
            food_times[stack] -= 1
            k -= 1
            if k == -1:
                return stack+1
            start_end = 0

        # print(food_times)
        ## stack 증가시키기 
        stack += 1
        if stack == len(food_times):
            stack = 0

print(solution([0, 0, 0, 0], 3))