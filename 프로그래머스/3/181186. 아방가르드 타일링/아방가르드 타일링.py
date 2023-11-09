def solution(n):
    d = [0] * 100001
    d[1] = 1
    d[2] = 3
    d[3] = 10
    d[4] = 23
    d[5] = 62
    d[6] = 170
    
    for i in range(7, n+1):
        d[i] = (d[i-1] + 2 * d[i-2] + 6 * d[i-3] + d[i-4] - d[i-6]) % 1000000007
    
    return d[n]