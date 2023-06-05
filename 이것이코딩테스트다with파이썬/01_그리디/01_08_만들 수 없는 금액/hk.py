def solution(n,array):

    temp_list = sorted(array)
    print(temp_list)

    dic = {}
    li = [0]

    for i in range(len(temp_list)):
        for l in range(len(li)):
            if not dic.get(li[l] + temp_list[i]):
                dic[li[l] + temp_list[i]] = 1
                li.append(li[l] + temp_list[i])

    stack = 1
    while True:
        if not dic.get(stack):
            return stack
        stack += 1

print(solution(5,[3,2,1,1,9]))