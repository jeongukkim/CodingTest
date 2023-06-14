def solution(n,k,apple,l,info):
    answer = 0

    li = [[0]*n for i in range(n)]

    for i in apple:
        a,b = map(int,i.split())
        li[a-1][b-1] = 1
    
    print(*li, sep='\n')

    loce = (0,0)
    arrow = (0,1)
    start_time = 0

    def lote(ar,lo):
        if lo == 'D':
            if ar == (0,1):
                return (1,0)
            elif ar == (1,0):
                return (0,-1)
            elif ar == (0,-1):
                return (-1,0)
            elif ar == (-1,0):
                return (0,1)
        elif lo == 'L':
            if ar == (0,1):
                return (-1,0)
            elif ar == (1,0):
                return (0,1)
            elif ar == (0,-1):
                return (1,0)
            elif ar == (-1,0):
                return (0,-1)



    dic = {}

    for i in info:
        a,b = i.split()
        a = int(a)
        dic[a] = b


    print(loce)
    loce = (loce[0]+arrow[0],loce[1]+arrow[1])
    print(loce)

    # while True:
    #     if loce[0] < 0 or loce[0] >= n or loce[1] < 0 or loce[1] >= n:
    #         break
    #     if li[loce[0]][loce[1]] == 1:




    return answer

print(solution(6,3,["3 4",
                    "2 5",
                    "5 3"],
                    3,["3 D",
                    "15 L",
                    "17 D"]))