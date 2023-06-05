def solution(s):
    answer = 0

    zero = 0
    one = 0

    pre = -1
    for i in s:
        temp = int(i)
        if temp == 0:
            if temp != pre:
                zero += 1
        else:
            if temp != pre:
                one += 1
        
        pre = temp

    # print(zero,one)
    
    return min(zero,one)

## print(solution("0001100"))