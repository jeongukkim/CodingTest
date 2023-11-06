from typing import List


def solution(citations: List[int]):
    answer:int = 0
    
    start:int = 0
    end:int = max(citations)
    
    while start <= end:
        mid:int = (start + end) // 2
        num_papers:int = 0
        
        for c in citations:
            if c >= mid:
                num_papers += 1
        
        if mid <= num_papers:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1
    
    return answer