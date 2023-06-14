[01 당장 좋은 것만 선택하는 그리디](https://trinityforce.tistory.com/entry/%EC%9D%B4%EA%B2%83%EC%9D%B4-%EC%BD%94%EB%94%A9-%ED%85%8C%EC%8A%A4%ED%8A%B8%EB%8B%A4-with-%ED%8C%8C%EC%9D%B4%EC%8D%AC-1-%EB%8B%B9%EC%9E%A5-%EC%A2%8B%EC%9D%80-%EA%B2%83%EB%A7%8C-%EC%84%A0%ED%83%9D%ED%95%98%EB%8A%94-%EA%B7%B8%EB%A6%AC%EB%94%94/)

[02 아이디어를 코드로 바꾸는 구현](https://trinityforce.tistory.com/entry/02-%EC%95%84%EC%9D%B4%EB%94%94%EC%96%B4%EB%A5%BC-%EC%BD%94%EB%93%9C%EB%A1%9C-%EB%B0%94%EA%BE%B8%EB%8A%94-%EA%B5%AC%EA%B5%AC%ED%98%84)

[03 꼭 필요한 자료구조 탐색 알고리즘 DFS/BFS](https://trinityforce.tistory.com/entry/03-%EA%BC%AD-%ED%95%84%EC%9A%94%ED%95%9C-%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%ED%83%90%EC%83%89-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-DFSBFS)

[04 기준에 따라 데이터를 정렬](https://trinityforce.tistory.com/entry/04-%EA%B8%B0%EC%A4%80%EC%97%90-%EB%94%B0%EB%9D%BC-%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%A5%BC-%EC%A0%95%EB%A0%AC)

[05 범위를 반씩 좁혀가는 탐색](https://trinityforce.tistory.com/entry/05-%EB%B2%94%EC%9C%84%EB%A5%BC-%EB%B0%98%EC%94%A9-%EC%A2%81%ED%98%80%EA%B0%80%EB%8A%94-%ED%83%90%EC%83%89)

[06 다이나믹 프로그래밍](https://trinityforce.tistory.com/entry/06-%EB%8B%A4%EC%9D%B4%EB%82%98%EB%AF%B9-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)

[07 가장 빠른 길 찾기](https://trinityforce.tistory.com/entry/07-%EA%B0%80%EC%9E%A5-%EB%B9%A0%EB%A5%B8-%EA%B8%B8-%EC%B0%BE%EA%B8%B0)

[08 다양한 그래프 알고리즘](https://trinityforce.tistory.com/entry/08-%EB%8B%A4%EC%96%91%ED%95%9C-%EA%B7%B8%EB%9E%98%ED%94%84-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98)

# \[문제\]

고고학자인 **"튜브"** 는 고대 유적지에서 보물과 유적이 가득할 것으로 추정되는 비밀의 문을 발견하였습니다. 그런데 문을 열려고 살펴보니 특이한 형태의 자물쇠로 잠겨 있었고 문 앞에는 특이한 형태의 열쇠와 함께 자물쇠를 푸는 방법에 대해 다음과 같이 설명해 주는 종이가 발견되었습니다.

잠겨있는 자물쇠는 격자 한 칸의 크기가 1 x 1인 N x N 크기의 정사각 격자 형태이고 특이한 모양의 열쇠는 M x M 크기인 정사각 격자 형태로 되어 있습니다.

자물쇠에는 홈이 파여 있고 열쇠 또한 홈과 돌기 부분이 있습니다. 열쇠는 회전과 이동이 가능하며 열쇠의 돌기 부분을 자물쇠의 홈 부분에 딱 맞게 채우면 자물쇠가 열리게 되는 구조입니다. 자물쇠 영역을 벗어난 부분에 있는 열쇠의 홈과 돌기는 자물쇠를 여는 데 영향을 주지 않지만, 자물쇠 영역 내에서는 열쇠의 돌기 부분과 자물쇠의 홈 부분이 정확히 일치해야 하며 열쇠의 돌기와 자물쇠의 돌기가 만나서는 안됩니다. 또한 자물쇠의 모든 홈을 채워 비어있는 곳이 없어야 자물쇠를 열 수 있습니다.

열쇠를 나타내는 2차원 배열 key와 자물쇠를 나타내는 2차원 배열 lock이 매개변수로 주어질 때, 열쇠로 자물쇠를 열수 있으면 true를, 열 수 없으면 false를 return 하도록 solution 함수를 완성해주세요.

# \[제한 사항\]

-   key는 M x M(3 ≤ M ≤ 20, M은 자연수)크기 2차원 배열입니다.
-   lock은 N x N(3 ≤ N ≤ 20, N은 자연수)크기 2차원 배열입니다.
-   M은 항상 N 이하입니다.
-   key와 lock의 원소는 0 또는 1로 이루어져 있습니다.
    -   0은 홈 부분, 1은 돌기 부분을 나타냅니다.

# \[입출력 예시\]

| key | lock | result |
| --- | --- | --- |
| \[\[0, 0, 0\], \[1, 0, 0\], \[0, 1, 1\]\] | \[\[1, 1, 1\], \[1, 1, 0\], \[1, 0, 1\]\] | true |