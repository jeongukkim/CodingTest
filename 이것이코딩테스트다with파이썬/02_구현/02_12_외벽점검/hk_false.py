def solution(n, weak, dist):
    dist = sorted(dist,reverse = True)
    
    ## 모든 경우의 수
    
    ## 일꾼 거리, 남은 취약점 리스트
    def go(d,w_li):
        temp_li = []
        for i in w_li:
            temp = []
            start = i
            end = i+d
            
            ## 취약점들에서 못가는곳 반환
            
            ## 전체길이보다 짧다면
            if end < n:
                for ii in w_li:
                    if ii < start or end < ii:
                        temp.append(ii)
                
            ## 전체길이와 같거나 길다면
            else:
                for ii in w_li:
                    if end-n < ii < start:
                        temp.append(ii)
            
            if temp:
                temp_li.append(temp)
            
            ## 전체 취약점이 완료되었으므로
            else:
                return False
            
        return temp_li
    
    li = go(dist[0],weak)

    ## False 라면
    if not li:
        return 1
    
    for stack in range(1,len(dist)):
        temp_li = []
        maxli = 0
        for i in li:
            temp = go(dist[stack],i)
            if not temp:
                return stack + 1
            else:
                temp_li += temp
        li = temp_li

    
    return -1

print(solution(12,[1, 5, 6, 10],[1, 2, 3, 4]))

## 테케 13만 통과를 못함, 시간초과