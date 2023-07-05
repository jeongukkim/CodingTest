## 첫 번째 줄에 얼음 틀의 세로 길이 N과 가로 길이 M이 주어진다. (1 <= N, M <= 1,000)

def solution(n,array):
    answer = 0
    
    len_y = n[0]
    len_x = n[1]


    # ## x 부터 하고 y 하기 때문 가로부터
    # ## 그다음 세로 우선으로 

    # for y in range(len_y):
    #     for x in range(len_x):
    #         if array[y][x] == 0:
                
    ## 깊이 우선 탐색
    def dfs(y, x):
        if x <= -1 or x >= len_x or y <= -1 or y >= len_y:
            return False
        ## 0 이면 1로 바꾸기
        if array[y][x] == 0:
            array[y][x] = 1
            dfs(y - 1, x)
            dfs(y, x - 1)
            dfs(y + 1, x)
            dfs(y, x + 1)
            return True
        
        return False
    
    for i in range(len_y):
        for j in range(len_x):
            if dfs(i, j) == True:
                answer += 1

    print(answer)
    return answer

print(solution((4,5),
[[0,0,1,1,0],
[0,0,0,1,1],
[1,1,1,1,1],
[0,0,0,0,0]]))