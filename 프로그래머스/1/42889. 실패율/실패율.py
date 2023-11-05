def solution(N, stages):
    answer = []
    
    users = len(stages)
    for i in range(1, N+1):
        count = stages.count(i)
        
        if users == 0: fail = 0
        else: fail = count / users
        
        answer.append((i, fail))
        users -= count
    
    answer.sort(key=lambda x: x[1], reverse=True)
    
    answer = [x[0] for x in answer]
    return answer