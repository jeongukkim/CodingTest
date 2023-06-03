[01 당장 좋은 것만 선택하는 그리디](https://trinityforce.tistory.com/entry/%EC%9D%B4%EA%B2%83%EC%9D%B4-%EC%BD%94%EB%94%A9-%ED%85%8C%EC%8A%A4%ED%8A%B8%EB%8B%A4-with-%ED%8C%8C%EC%9D%B4%EC%8D%AC-1-%EB%8B%B9%EC%9E%A5-%EC%A2%8B%EC%9D%80-%EA%B2%83%EB%A7%8C-%EC%84%A0%ED%83%9D%ED%95%98%EB%8A%94-%EA%B7%B8%EB%A6%AC%EB%94%94/)

[02 아이디어를 코드로 바꾸는 구현](https://trinityforce.tistory.com/entry/02-%EC%95%84%EC%9D%B4%EB%94%94%EC%96%B4%EB%A5%BC-%EC%BD%94%EB%93%9C%EB%A1%9C-%EB%B0%94%EA%BE%B8%EB%8A%94-%EA%B5%AC%EA%B5%AC%ED%98%84)

[03 꼭 필요한 자료구조 탐색 알고리즘 DFS/BFS](https://trinityforce.tistory.com/entry/03-%EA%BC%AD-%ED%95%84%EC%9A%94%ED%95%9C-%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%ED%83%90%EC%83%89-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-DFSBFS)

[04 기준에 따라 데이터를 정렬](https://trinityforce.tistory.com/entry/04-%EA%B8%B0%EC%A4%80%EC%97%90-%EB%94%B0%EB%9D%BC-%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%A5%BC-%EC%A0%95%EB%A0%AC)

[05 범위를 반씩 좁혀가는 탐색](https://trinityforce.tistory.com/entry/05-%EB%B2%94%EC%9C%84%EB%A5%BC-%EB%B0%98%EC%94%A9-%EC%A2%81%ED%98%80%EA%B0%80%EB%8A%94-%ED%83%90%EC%83%89)

[06 다이나믹 프로그래밍](https://trinityforce.tistory.com/entry/06-%EB%8B%A4%EC%9D%B4%EB%82%98%EB%AF%B9-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)

[07 가장 빠른 길 찾기](https://trinityforce.tistory.com/entry/07-%EA%B0%80%EC%9E%A5-%EB%B9%A0%EB%A5%B8-%EA%B8%B8-%EC%B0%BE%EA%B8%B0)

[08 다양한 그래프 알고리즘](https://trinityforce.tistory.com/entry/08-%EB%8B%A4%EC%96%91%ED%95%9C-%EA%B7%B8%EB%9E%98%ED%94%84-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98)

## \[문제\]

한 마을에 모험가가 N명 있습니다. 모험가 길드에서는 N명의 모험가를 대상으로 '공포도'를 측정했는데, '공포도'가 높은  
모험가는 쉽게 공포를 느껴 위험 상황에서 제대로 대처할 능력이 떨어집니다.  
모험가 길드장인 동빈이는 모험가 그룹을 안전하게 구성하고자 공포도가 X인 모험가는 반드시 X명 이상으로 구성한  
모험가 그룹에 참여해야 여행을 떠날 수 있도록 규정했습니다.  
동빈이는 최대 몇 개의 모험가 그룹을 만들 수 있는지 궁금합니다. N명의 모험가에 대한 정보가 주어졌을 때,  
여행을 떠날 수 있는 그룹 수의 최댓값을 구하는 프로그램을 작성하세요.  
  
이때, 몇 명의 모험가는 마을에 그대로 남아 있어도 되기 때문에, 모든 모험가를 특정한 그룹에 넣을 필요는 없습니다.  
  

## \[입력 조건\]

-   첫째 줄에 모험가의 수 N이 주어집니다. (1 <= N <= 100,000)
-   둘째 줄에 각 모험가의 공포도의 값을 N 이하의 자연수로 주어지며, 각 자연수는 공백으로 구분합니다.

## \[출력 조건\]

-   여행을 떠날 수 있는 그룹 수의 최댓값을 출력합니다.

###   
입력 예시

```

5
2 3 1 2 2
```

###   
출력 예시

```
2
```
