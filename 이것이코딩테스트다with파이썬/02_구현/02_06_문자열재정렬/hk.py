def solution(n):

    st = ""
    nu = 0

    for i in n:
        temp = ord(i)
        if 65 <= temp:
            st += i
        else:
            nu += int(i)

    return "".join(sorted(st)) + str(nu)

print(solution("K1KA5CB7"))