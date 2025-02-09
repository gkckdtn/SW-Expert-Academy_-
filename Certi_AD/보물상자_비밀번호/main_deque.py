import sys
from collections import deque

sys.stdin = open("sample_input.txt", "r")

T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    pw = deque(input())  # `deque` 사용하여 리스트 변환
    cnt = N // 4  # 한 변당 숫자 개수

    arr = set()  # 중복 제거를 위해 `set` 사용

    for _ in range(cnt):  # `cnt`번 회전
        for j in range(0, N, cnt):  # `cnt` 간격으로 숫자 추출
            temp_list = list(pw)
            arr.add(str("".join(temp_list[j:j+cnt])))  # 16진수 숫자 만들고 set에 추가

        pw.rotate(1)  # `deque`를 사용하여 한 칸 회전 (O(1))

    answer = sorted([int(num, 16) for num in arr], reverse=True)  # 10진수 변환 & 정렬
    print(f'#{t+1} {answer[K-1]}')  # K번째 큰 수 출력

