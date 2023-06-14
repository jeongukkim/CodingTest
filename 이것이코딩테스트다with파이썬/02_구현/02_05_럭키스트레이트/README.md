[01 당장 좋은 것만 선택하는 그리디](https://trinityforce.tistory.com/entry/%EC%9D%B4%EA%B2%83%EC%9D%B4-%EC%BD%94%EB%94%A9-%ED%85%8C%EC%8A%A4%ED%8A%B8%EB%8B%A4-with-%ED%8C%8C%EC%9D%B4%EC%8D%AC-1-%EB%8B%B9%EC%9E%A5-%EC%A2%8B%EC%9D%80-%EA%B2%83%EB%A7%8C-%EC%84%A0%ED%83%9D%ED%95%98%EB%8A%94-%EA%B7%B8%EB%A6%AC%EB%94%94/)

[02 아이디어를 코드로 바꾸는 구현](https://trinityforce.tistory.com/entry/02-%EC%95%84%EC%9D%B4%EB%94%94%EC%96%B4%EB%A5%BC-%EC%BD%94%EB%93%9C%EB%A1%9C-%EB%B0%94%EA%BE%B8%EB%8A%94-%EA%B5%AC%EA%B5%AC%ED%98%84)

[03 꼭 필요한 자료구조 탐색 알고리즘 DFS/BFS](https://trinityforce.tistory.com/entry/03-%EA%BC%AD-%ED%95%84%EC%9A%94%ED%95%9C-%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%ED%83%90%EC%83%89-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-DFSBFS)

[04 기준에 따라 데이터를 정렬](https://trinityforce.tistory.com/entry/04-%EA%B8%B0%EC%A4%80%EC%97%90-%EB%94%B0%EB%9D%BC-%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%A5%BC-%EC%A0%95%EB%A0%AC)

[05 범위를 반씩 좁혀가는 탐색](https://trinityforce.tistory.com/entry/05-%EB%B2%94%EC%9C%84%EB%A5%BC-%EB%B0%98%EC%94%A9-%EC%A2%81%ED%98%80%EA%B0%80%EB%8A%94-%ED%83%90%EC%83%89)

[06 다이나믹 프로그래밍](https://trinityforce.tistory.com/entry/06-%EB%8B%A4%EC%9D%B4%EB%82%98%EB%AF%B9-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)

[07 가장 빠른 길 찾기](https://trinityforce.tistory.com/entry/07-%EA%B0%80%EC%9E%A5-%EB%B9%A0%EB%A5%B8-%EA%B8%B8-%EC%B0%BE%EA%B8%B0)

[08 다양한 그래프 알고리즘](https://trinityforce.tistory.com/entry/08-%EB%8B%A4%EC%96%91%ED%95%9C-%EA%B7%B8%EB%9E%98%ED%94%84-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98)

# \[문제\]

어떤 게임의 아웃복서 캐릭터에게는 럭키 스트레이트라는 기술이 존재한다. 이 기술은 매우 강력한 대신에 항상 사용할 수는 없으며, 현재 게임 내에서 점수가 특정 조건을 만족할 때만 사용할 수 있다.

특정 조건이란 현재 캐릭터의 점수를 N이라고 할 때 점수 N을 자릿수를 기준으로 반으로 나누어 왼쪽 부분의 각 자릿수의 합과 오른쪽 부분의 각 자릿수의 합을 더한 값이 동일한 상황을 의미한다. 예를 들어 현재 점수가 123,402라면 왼쪽 부분의 각 자릿수의 합은 1+2+3, 오른쪽 부분의 각 자릿수의 합은 4+0+2이므로 두 합이 6으로 동일하여 럭키 스트레이트를 사용할 수 있다.

현재 점수 N이 주어졌을 때, 럭키 스트레이트를 사용할 수 있는 상태인지 아닌지를 알려주는 프로그램을 작성하시오. 럭키 스트레이트를 사용할 수 있다면 "LUCKY"를, 사용할 수 없다면 "READY"라는 단어를 출력한다. 또한 점수 N의 자릿수는 항상 짝수 형태로만 주어진다. 예를 들어 자릿수가 5인 12,345와 같은 수는 입력으로 들어오지 않는다.

# \[입력 조건\]

-   첫째 줄에 점수 N이 정수로 주어진다. (10 ≤ N ≤ 99,999,999) 단, 점수 N의 자릿수는 항상 짝수 형태로만 주어진다.

# \[출력 조건\]

-   첫째 줄에 럭키 스트레이트를 사용할 수 있다면 "LUCKY"를, 사용할 수 없다면 "READY"라는 단어를 출력한다.입력예시1

## 입력예시1

```
123402
```

## 출력예시1

```
LUCKY
```

## 입력예시2

```
7755
```

## 출력예시2

```
READY
```