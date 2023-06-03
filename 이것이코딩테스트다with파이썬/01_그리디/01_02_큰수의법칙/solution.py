import time
import importlib

people = ["hk"]

test_cases = [
    (5, 8, 3, [2, 4, 5, 4, 6]),
    (5, 7, 2, [3, 4, 3, 4, 3]),
    (4, 6, 2, [1, 2, 3, 4]),
    (3, 4, 1, [10, 9, 8]),
    (10, 10, 5, [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]),
]

results = [
    46,
    28,
    22,
    38,
    50,
]



## 사람 임포트 함수
def load_module_func(module_name):
	tmp = importlib.import_module(module_name)
	return tmp

## 답 비교 함수
def load_answer_func(name):
    answer_count = 0
    answer_time = 0
    for n,i in enumerate(test_cases):
        start = time.time()
        if type(i) is tuple:
            temp_answer = name.solution(*i)
        else:
            temp_answer = name.solution(i)
        print("---------------------------------------")
        print(f"테스트 > {n+1}")
        print(f"입력값 > {i}")
        print(f"기댓값 > {results[n]}")
        if results[n] == temp_answer:
            print("테스트를 통과하였습니다.")
            answer_count += 1
        else: 
            print(f"실행 결과 > 실행한 결괏값 {temp_answer}이 기댓값 {results[n]}과 다릅니다.")
        
        temp_time = time.time() - start
        answer_time += temp_time
        print("time :", temp_time)


    if len(test_cases) == answer_count:
        print(f"경과 시간 {answer_time}")
        print("전부 맞았습니다!!")

for p in people:
    temp_import = load_module_func(p)
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print(f"{p}님 채점을 시작합니다.")
    load_answer_func(temp_import)
