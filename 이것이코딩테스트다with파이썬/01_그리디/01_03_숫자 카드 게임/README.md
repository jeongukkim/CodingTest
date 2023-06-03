[01 당장 좋은 것만 선택하는 그리디](https://trinityforce.tistory.com/entry/%EC%9D%B4%EA%B2%83%EC%9D%B4-%EC%BD%94%EB%94%A9-%ED%85%8C%EC%8A%A4%ED%8A%B8%EB%8B%A4-with-%ED%8C%8C%EC%9D%B4%EC%8D%AC-1-%EB%8B%B9%EC%9E%A5-%EC%A2%8B%EC%9D%80-%EA%B2%83%EB%A7%8C-%EC%84%A0%ED%83%9D%ED%95%98%EB%8A%94-%EA%B7%B8%EB%A6%AC%EB%94%94/)

[02 아이디어를 코드로 바꾸는 구현](https://trinityforce.tistory.com/entry/02-%EC%95%84%EC%9D%B4%EB%94%94%EC%96%B4%EB%A5%BC-%EC%BD%94%EB%93%9C%EB%A1%9C-%EB%B0%94%EA%BE%B8%EB%8A%94-%EA%B5%AC%EA%B5%AC%ED%98%84)

[03 꼭 필요한 자료구조 탐색 알고리즘 DFS/BFS](https://trinityforce.tistory.com/entry/03-%EA%BC%AD-%ED%95%84%EC%9A%94%ED%95%9C-%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%ED%83%90%EC%83%89-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-DFSBFS)

[04 기준에 따라 데이터를 정렬](https://trinityforce.tistory.com/entry/04-%EA%B8%B0%EC%A4%80%EC%97%90-%EB%94%B0%EB%9D%BC-%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%A5%BC-%EC%A0%95%EB%A0%AC)

[05 범위를 반씩 좁혀가는 탐색](https://trinityforce.tistory.com/entry/05-%EB%B2%94%EC%9C%84%EB%A5%BC-%EB%B0%98%EC%94%A9-%EC%A2%81%ED%98%80%EA%B0%80%EB%8A%94-%ED%83%90%EC%83%89)

[06 다이나믹 프로그래밍](https://trinityforce.tistory.com/entry/06-%EB%8B%A4%EC%9D%B4%EB%82%98%EB%AF%B9-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)

[07 가장 빠른 길 찾기](https://trinityforce.tistory.com/entry/07-%EA%B0%80%EC%9E%A5-%EB%B9%A0%EB%A5%B8-%EA%B8%B8-%EC%B0%BE%EA%B8%B0)

[08 다양한 그래프 알고리즘](https://trinityforce.tistory.com/entry/08-%EB%8B%A4%EC%96%91%ED%95%9C-%EA%B7%B8%EB%9E%98%ED%94%84-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98)

# **\[문제\]**

숫자 카드 게임은 여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임이다. 단, 게임의 룰을 지키며 카드를 뽑아야 하고 룰은 다음과 같다.

1.  숫자가 쓰인 카드들이 N x M 형태로 놓여 있다. 이때 N은 행의 개수를 의미하며, M은 열의 개수를 의미한다.
2.  먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택한다.
3.  그다음 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 한다.
4.  따라서 처음에 카드를 골라낼 행을 선택할 때, 이후에 해당 행에서 가장 숫자가 낮은 카드를 뽑을 것을 고려하여 최종적으로 갖아 높은 숫자의 카드를 뽑을 수 있도록 전략을 세워야 한다.

예를 들어 3x3 형태로 카드들이 다음과 같이 놓여 있다고 가정하자.

![https://blog.kakaocdn.net/dn/cYVsBD/btq3YT5clTm/kLEnhsLPIOXLYaxgsiKQm1/img.png](https://blog.kakaocdn.net/dn/cYVsBD/btq3YT5clTm/kLEnhsLPIOXLYaxgsiKQm1/img.png)

여기서 카드를 골라낼 행을 고를 때 첫 번째 혹은 두 번째 행을 선택하는 경우, 최종적으로 뽑는 카드는 1이다. 하지만 세 번째 행을 선택하는 경우 최종적으로 뽑는 카드는 2이다. 따라서 이 예제에서는 세 번째 행을 선택하여 숫자 2가 쓰여진 카드를 뽑는 것이 정답이다.

카드 N x M 형태로 놓여 있을 때, 게임의 룰에 맞게 카드를 뽑는 프로그램을 만드시오.

# **\[입력 조건\]**

-   첫째 줄에 숫자 카드들이 놓인 행의 개수 N과 열의 개수 M이 공백을 기준으로 하여 각각 자연수로 주어진다. (1 ≤ N.M ≤ 100)
-   둘째 줄에 N개의 줄에 걸쳐 각 카드에 적힌 숫자가 주어진다. 각 숫자는 1 이상 10,000 이하의 자연수이다.

# **\[출력 조건\]**

-   첫째 줄에 게임의 룰에 맞게 선택한 카드가 적힌 숫자를 출력한다.

### 입력 예시1

```

3 3
3 1 2
4 1 4
2 2 2
```

### 출력 예시1

```

2
```

### 입력 예시2

```

2 4
7 3 1 8
3 3 3 4
```

### 출력 예시2

```

3
```
