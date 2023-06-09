def solution(n,k):
    result = 0

    while n >= k:
        # N이 K로 나누어 떨어지지 않는다면 N에서 1씩 빼기
        while n % k != 0:
            n -= 1
            result += 1
        # K로 나누기
        n //= k
        result += 1

    # 마지막으로 남은 수에 대하여 1씩 빼기
    while n > 1:
        n -= 1
        result += 1
    return result

# print(25,5)