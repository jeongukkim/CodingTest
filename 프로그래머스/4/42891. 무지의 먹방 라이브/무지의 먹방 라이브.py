import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    q = []
    for i, time in enumerate(food_times):
        heapq.heappush(q, (time, i+1))
    
    used_time = prev = 0
    num_food = len(food_times)
    
    while used_time + (q[0][0] - prev) * num_food <= k:
        now = heapq.heappop(q)[0]
        used_time += (now - prev) * num_food
        num_food -= 1
        prev = now
    
    answer = sorted(q, key=lambda x: x[1])
    return answer[(k - used_time) % num_food][1]