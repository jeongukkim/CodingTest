def solution(n,array):
    answer = 0
    
    im = [1,1]

    def go(w):
        if w == "R":
            if im[1] < n:
                im[1] += 1
        if w == "L":
            if im[1] > 1:
                im[1] -= 1
        if w == "U":
            if im[0] > 1:
                im[0] -= 1
        if w == "D":
            if im[0] < n:
                im[0] += 1

    for i in array:
        go(i)

    
    return (im[0],im[1])

print(solution(5,["R","R","R","U","D","D"]))