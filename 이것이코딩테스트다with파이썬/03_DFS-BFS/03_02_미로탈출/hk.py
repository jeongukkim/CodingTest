## 현재 위치 (1,1)
## 출구 (오른쪽 끝)

def solution(n,m,array):
    from collections import deque
    answer = 0
    
    len_x = m
    len_y = n
    

    ## 왼 오 위 아래
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    

    ## 너비 우선 탐색
    def bfs(y, x):
        queue = deque()
        queue.append((y,x))
        while queue:
            y,x = queue.popleft()
            print(y,x)
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < len_x and 0 <= ny < len_y and array[ny][nx] == 1:
                    array[ny][nx] = array[y][x] + 1
                    queue.append((ny,nx))
        return array[len_y-1][len_x-1]   


    x = list(map(int,"00001"))



    print(x)


    return bfs(0,0)

print(solution(5,6,
[[1,0,1,0,1,0],
[1,1,1,1,1,1],
[0,0,0,0,0,1],
[1,1,1,1,1,1],
[1,1,1,1,1,1]]))