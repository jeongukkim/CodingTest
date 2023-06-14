def solution(key,lock):
    answer = True
    
    for i in key:
        print(i)

    print("asas")

    for i in lock:
        print(i)


    return answer

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))