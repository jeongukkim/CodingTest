def solution(a, b, g, s, w, t):
    num_city = len(g)
    
    start = 0
    end = 1e14 * 4
    
    answer = -1
    while start <= end:
        mid = (start + end) // 2
        
        gold_total = silver_total = mineral_total = 0
        for i in range(num_city):
            num_move = (mid // (2 * t[i])) if mid % (2 * t[i]) < t[i] else (mid // (2 * t[i])) + 1
            mineral_out = w[i] * num_move
            gold_total += min(mineral_out, g[i])
            silver_total += min(mineral_out, s[i])
            mineral_total += min(mineral_out, g[i] + s[i])
        
        if gold_total >= a and silver_total >= b and mineral_total >= a + b:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
    
    return answer