def possible(answer):
    for x, y, a in answer:
        if a == 0:
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            return False
        elif a == 1:
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            return False
    return True


def solution(n, build_frame):
    answer = []
    for x, y, a, b in build_frame:
        if b == 0:
            answer.remove([x, y, a])
            if not possible(answer):
                answer.append([x, y, a])
        if b == 1:
            answer.append([x, y, a])
            if not possible(answer):
                answer.pop()
    answer.sort(key=lambda x: (x[0], x[1], x[2]))
    
    return answer