import sys
from collections import deque

sys.stdin = open('sample_input.txt')

for tc in range(1, int(input()) + 1):
    # 입력 받기
    N, M, K, A, B = map(int, input().split())  # 접수 창구 개수, 정비 창구 개수, 방문 고객 수, 지갑 두고간 접수 창구, 정비 창구
    A -= 1  # 인덱스 맞추기
    B -= 1
    reception_time = list(map(int, input().split()))  # 접수 창구 처리 시간
    repair_time = list(map(int, input().split()))  # 정비 창구 처리 시간
    arrival_times = list(map(int, input().split()))  # 각 고객 도착 시간

    # **Step 1: 접수 창구 배정 (Greedy)**
    reception_queue = deque()  # 접수 창구 대기열
    reception_status = [None] * N  # 각 창구에서 현재 처리 중인 고객 정보 (None이면 비어있음)
    reception_end_time = [0] * N  # 창구별 처리 끝나는 시간
    reception_customers = []  # (접수 완료 시간, 접수 창구 번호, 고객 번호)

    time = 0  # 현재 시간
    customer_index = 0  # 고객 인덱스
    while customer_index < K or reception_queue or any(reception_status):
        # 1. 현재 시간에 도착한 고객이 있으면 접수 대기열에 추가
        while customer_index < K and arrival_times[customer_index] == time:
            reception_queue.append(customer_index)
            customer_index += 1

        # 2. 접수 창구에서 고객 처리 (가장 빠른 창구부터)
        for i in range(N):
            if reception_status[i] is not None and reception_end_time[i] == time:
                reception_customers.append((time, i, reception_status[i]))  # (완료 시간, 창구 번호, 고객 번호)
                reception_status[i] = None  # 창구 비우기

        # 3. 빈 접수 창구가 있으면 고객 배정
        for i in range(N):
            if reception_status[i] is None and reception_queue:
                customer = reception_queue.popleft()
                reception_status[i] = customer  # 창구에 고객 배정
                reception_end_time[i] = time + reception_time[i]  # 종료 시간 갱신

        time += 1

    # **Step 2: 정비 창구 배정**
    reception_customers.sort()  # 접수 완료 시간을 기준으로 정렬 (FIFO)
    repair_queue = deque(reception_customers)  # 정비 창구 대기열
    repair_status = [None] * M  # 정비 창구 상태
    repair_end_time = [0] * M  # 창구별 처리 끝나는 시간
    repair_customers = []  # (정비 완료 시간, 접수 창구 번호, 정비 창구 번호, 고객 번호)

    time = 0
    while repair_queue or any(repair_status):
        # 1. 정비 창구에서 고객 처리 완료
        for i in range(M):
            if repair_status[i] is not None and repair_end_time[i] == time:
                repair_customers.append((time, repair_status[i][1], i, repair_status[i][0]))  # (완료 시간, 접수 창구, 정비 창구, 고객)
                repair_status[i] = None

        # 2. 빈 정비 창구가 있으면 고객 배정
        for i in range(M):
            if repair_status[i] is None and repair_queue and repair_queue[0][0] <= time:
                _, reception_desk, customer = repair_queue.popleft()
                repair_status[i] = (customer, reception_desk)  # (고객 번호, 접수 창구)
                repair_end_time[i] = time + repair_time[i]  # 종료 시간 갱신

        time += 1

    # **Step 3: 결과 계산**
    result = sum(cust + 1 for end_time, rec, rep, cust in repair_customers if rec == A and rep == B)
    if result == 0:
        result = -1

    print(f'#{tc} {result}')
