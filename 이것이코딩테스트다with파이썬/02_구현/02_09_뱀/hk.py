from collections import deque

def solution(n,k,apple,l,info):
    ### 가정 : 중복된 시간으로 방향을 바꾸는 경우는 없다.

    ## n = 보드의 크기
    ## k = 사과의 개수
    ## apple = 사과의 위치
    ## l = 뱀의 방향 변환 횟수
    ## info = 뱀의 방향 변환 정보

    ## 보드 만들기
    li = [[0]*n for i in range(n)]

    ## 사과 보드에 넣기
    for i in apple:
        a,b = map(int,i.split())
        li[a-1][b-1] = 1
    
    # print(*li, sep='\n')

    ## 방향 변환 정보 딕셔너리 info_dic[시간] = 방향
    info_dic = {}
    for i in info:
        a,b = i.split()
        a = int(a)
        info_dic[a] = b

    ## 뱀의 위치, 방향, 시작 시간
    ## 오른쪽으로 한칸가놓고 시작은 1초로 한다.

    ## [direction] 0 = 우, 1 = 하, 2 = 좌, 3 = 상
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    snake = deque()  # 뱀의 위치
    snake.append((0, 0))  # 뱀의 초기 위치
    direction = 0  # 초기 방향 (오른쪽)
    ## 시작하자마자 방향전환이 있다면
    if info_dic.get(0) == 'D':
        direction = 1
    elif info_dic.get(0) == 'L':
        ## 왼쪽으로가면 위에 쳐박음
        return 1
    
    time = 0  # 현재 시간

    while True:
        time += 1  # 시간 증가
        ## 뱀의 머리 위치 갈곳
        nx = snake[0][1] + dx[direction]
        ny = snake[0][0] + dy[direction]

        ## 박히거나 내 몸에 부딪히면 끝
        if nx < 0 or nx >= n or ny < 0 or ny >= n or (ny, nx) in snake:
            return time
        
        # 다음 위치에 사과가 있는지 확인
        if li[ny][nx] == 1:
            li[ny][nx] = 0  # 사과 제거
            snake.appendleft((ny, nx))  # 뱀의 머리 이동
        else:
            snake.appendleft((ny, nx))  # 뱀의 머리 이동
            snake.pop()  # 꼬리 제거
        
        ## 방향 전환
        if info_dic.get(time) == 'D':
            direction += 1
            if direction == 4:
                direction = 0
        elif info_dic.get(time) == 'L':
            direction -= 1
            if direction == -1:
                direction = 3

print(solution(6,3,["3 4",
                    "2 5",
                    "5 3"],
                    3,["3 D",
                    "15 L",
                    "17 D"]))