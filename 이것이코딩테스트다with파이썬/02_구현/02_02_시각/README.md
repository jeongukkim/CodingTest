[01 당장 좋은 것만 선택하는 그리디](https://trinityforce.tistory.com/entry/%EC%9D%B4%EA%B2%83%EC%9D%B4-%EC%BD%94%EB%94%A9-%ED%85%8C%EC%8A%A4%ED%8A%B8%EB%8B%A4-with-%ED%8C%8C%EC%9D%B4%EC%8D%AC-1-%EB%8B%B9%EC%9E%A5-%EC%A2%8B%EC%9D%80-%EA%B2%83%EB%A7%8C-%EC%84%A0%ED%83%9D%ED%95%98%EB%8A%94-%EA%B7%B8%EB%A6%AC%EB%94%94/)

[02 아이디어를 코드로 바꾸는 구현](https://trinityforce.tistory.com/entry/02-%EC%95%84%EC%9D%B4%EB%94%94%EC%96%B4%EB%A5%BC-%EC%BD%94%EB%93%9C%EB%A1%9C-%EB%B0%94%EA%BE%B8%EB%8A%94-%EA%B5%AC%EA%B5%AC%ED%98%84)

[03 꼭 필요한 자료구조 탐색 알고리즘 DFS/BFS](https://trinityforce.tistory.com/entry/03-%EA%BC%AD-%ED%95%84%EC%9A%94%ED%95%9C-%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%ED%83%90%EC%83%89-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-DFSBFS)

[04 기준에 따라 데이터를 정렬](https://trinityforce.tistory.com/entry/04-%EA%B8%B0%EC%A4%80%EC%97%90-%EB%94%B0%EB%9D%BC-%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%A5%BC-%EC%A0%95%EB%A0%AC)

[05 범위를 반씩 좁혀가는 탐색](https://trinityforce.tistory.com/entry/05-%EB%B2%94%EC%9C%84%EB%A5%BC-%EB%B0%98%EC%94%A9-%EC%A2%81%ED%98%80%EA%B0%80%EB%8A%94-%ED%83%90%EC%83%89)

[06 다이나믹 프로그래밍](https://trinityforce.tistory.com/entry/06-%EB%8B%A4%EC%9D%B4%EB%82%98%EB%AF%B9-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)

[07 가장 빠른 길 찾기](https://trinityforce.tistory.com/entry/07-%EA%B0%80%EC%9E%A5-%EB%B9%A0%EB%A5%B8-%EA%B8%B8-%EC%B0%BE%EA%B8%B0)

[08 다양한 그래프 알고리즘](https://trinityforce.tistory.com/entry/08-%EB%8B%A4%EC%96%91%ED%95%9C-%EA%B7%B8%EB%9E%98%ED%94%84-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98)

## \[문제\]

정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하시오. 예를 들어 1을 입력했을 때 다음은 3이 하나라도 포하모디어 있으므로 세어야 하는 시각이다.

-   00시 00분 03초
-   00시 13분 30초

반면에 다음은 3이 하나도 포함되어 있지 않으므로 세면 안 되는 시각이다.

-   00시 02분 55초
-   01시 27분 45초

## \[입력 조건\]

-   첫째 줄에 정수 N이 입력된다. (0 <= N <= 23)

## \[출력 조건\]

-   00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 출력한다.

### 입력 예시

```
5
```

###   
출력 예시

```
11475
```