
# 치킨 거리의 합을 계산하는 함수
def solution(n,m,graph):

    from itertools import combinations

    chicken, house = [], []

    for r in range(n):
        for c in range(n):
            if graph[r][c] == 1:
                house.append((r, c)) # 일반 집
            elif graph[r][c] == 2:
                chicken.append((r, c)) # 치킨집
    # print(chicken)
    # print(house)

    # 모든 치킨 집 중에서 m개의 치킨 집을 뽑는 조합 계산
    candidates = list(combinations(chicken, m))

    # print(candidates)

    def get_sum(candidate):
        result = 0
        # 모든 집에 대하여
        for hx, hy in house:
            # 가장 가까운 치킨 집을 찾기
            temp = 1e9
            for cx, cy in candidate:
                temp = min(temp, abs(hx - cx) + abs(hy - cy))
            # 가장 가까운 치킨 집까지의 거리를 더하기
            result += temp
        # 치킨 거리의 합 반환
        # print(result)
        return result

    # 치킨 거리의 합의 최소를 찾아 출력
    result = 1e9
    for candidate in candidates:
        result = min(result, get_sum(candidate))


    return result


# print(solution(5,3,[[0,0,1,0,0],
# [0,0,2,0,1],
# [0,1,2,0,0],
# [0,0,1,0,0],
# [0,0,0,0,2]]))