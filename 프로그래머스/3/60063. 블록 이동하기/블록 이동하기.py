from collections import deque


def get_next_pos(pos, board):
    next_pos = []
    pos = list(pos)
    ly, lx, ry, rx = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    for i in range(4):
        next_ly, next_lx, next_ry, next_rx = ly + dy[i], lx + dx[i], ry + dy[i], rx + dx[i]
        if not board[next_ly][next_lx] and not board[next_ry][next_rx]:
            next_pos.append({(next_ly, next_lx), (next_ry, next_rx)})
    # 세로로 서있는 경우
    if lx == rx:
        for i in [-1, 1]:
            if not board[ly][lx+i] and not board[ry][rx+i]:
                next_pos.append({(ly, lx), (ly, rx+i)})
                next_pos.append({(ry, lx), (ry, rx+i)})
    # 가로로 서있는 경우
    else:
        for i in [-1, 1]:
            if not board[ly+i][lx] and not board[ry+i][rx]:
                next_pos.append({(ly, lx), (ry+i, lx)})
                next_pos.append({(ly, rx), (ry+i, rx)})
    return next_pos
        

def solution(board):
    n = len(board)
    bounded_board = [[1] * (n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            bounded_board[i+1][j+1] = board[i][j]
    
    visited = []
    queue = deque()
    queue.append(({(1,1), (1,2)}, 0))
    visited.append({(1,1), (1,2)})
    while queue:
        pos, num = queue.popleft()
        if (n, n) in pos:
            return num
        for next_pos in get_next_pos(pos, bounded_board):
            if next_pos not in visited:
                queue.append((next_pos, num+1))
                visited.append(next_pos)
