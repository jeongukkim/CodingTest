def solution(n,k,array):
    
    a = array[0]
    b = array[1]


    for i in range(k):
        temp_min = min(a)
        temp_max = max(b)
        a[a.index(temp_min)] = temp_max
        b[b.index(temp_max)] = temp_min

    return sum(a)

# print(solution(5,3,[[1,2,5,4,3],[5,5,6,6,5]]))