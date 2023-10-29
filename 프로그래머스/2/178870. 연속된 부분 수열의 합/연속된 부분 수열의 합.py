def solution(sequence, k):
    answer = []
    s = e = 0
    partial_sum = sequence[0]
    while e < len(sequence) and s <= e:
        if partial_sum < k:
            e += 1
            if e == len(sequence): break
            partial_sum += sequence[e]
        elif partial_sum > k:
            partial_sum -= sequence[s]
            s += 1
            if s > e: break
        else:
            answer.append((s, e))
            e += 1
            if e == len(sequence): break
            partial_sum += sequence[e]
    answer.sort(key=lambda x: (x[1]-x[0], x[0]))
    return answer[0]
