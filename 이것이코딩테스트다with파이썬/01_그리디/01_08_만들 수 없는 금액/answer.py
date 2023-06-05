def solution(n,array):
    answer = 0

    array.sort()

    target = 1
    for x in array:
        # 만들 수 없는 금액을 찾았을 때 반복 종료
        if target < x:
            break
        target += x

    return target

# print(solution(4,[1,2,2,5]))