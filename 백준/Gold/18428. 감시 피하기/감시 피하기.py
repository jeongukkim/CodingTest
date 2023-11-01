import sys
input = sys.stdin.readline

n = int(input())
board, teachers = [], []
for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        if board[i][j] == 'T':
            teachers.append((i, j))
            
answer = "NO"


def watch(y, x, direction):
    if direction == 0:
        while x >= 0:
            if board[y][x] == 'S':
                return True
            if board[y][x] == 'O':
                return False
            x -= 1
    if direction == 1:
        while x < n:
            if board[y][x] == 'S':
                return True
            if board[y][x] == 'O':
                return False
            x += 1
    if direction == 2:
        while y >= 0:
            if board[y][x] == 'S':
                return True
            if board[y][x] == 'O':
                return False
            y -= 1
    if direction == 3:
        while y < n:
            if board[y][x] == 'S':
                return True
            if board[y][x] == 'O':
                return False
            y += 1
    return False


def dfs(count):
    global answer
    if count == 3:
        find = False
        for teacher in teachers:
            for dir in range(4):
                if watch(*teacher, dir):
                    find = True
        if not find: answer = "YES"
        return
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'X':
                board[i][j] = 'O'
                count += 1
                dfs(count)
                board[i][j] = 'X'
                count -= 1
            
dfs(0)
print(answer)
