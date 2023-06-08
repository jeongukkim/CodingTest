def solution(n):

    l = len(n)
    li = []
    
    for i in range(1,(l//2) + 1):
        answer = 0
        temp = 0
        pre = ""
        count = 1
        for ii in range(0,l,i):
            # print(n[temp:ii])
            if pre != "":
                if pre == n[temp:ii]:
                    count += 1
                else:
                    if count != 1:
                        answer += len(str(count)) + i
                    else:
                        answer += i
                    count = 1
        
            pre = n[temp:ii]
            temp = ii

        if pre == n[temp:]:
            count += 1
            answer += len(str(count)) + i
        else:
            answer += i + len(n[temp:])
        
        # print(pre,n[temp:])
        # print(answer)
        li.append(answer)

    return min(li)

print(solution("ababcdcdababcdcd"))