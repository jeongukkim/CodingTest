def solution(n,m,k):
    answer = 0

    dic = {}
    for i in k:
        if dic.get(i):
            dic[i] += 1
        else:
            dic[i] = 1
 

    for i in range(1,m+1):
        if dic.get(i):
            answer += (n-dic[i]) * dic[i]
            n -= dic[i]
        

    return answer

print(solution(5,3,[1,3,2,3,2]))