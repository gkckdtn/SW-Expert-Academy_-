import sys

sys.stdin = open('sample_input.txt')

for tc in range(1, int(input()) + 1):
    # 입력 처리
    N, M, K, A, B = map(int, input().split())
    A -= 1  # 인덱스 맞추기
    B -= 1
    reception_times = list(map(int, input().split()))  # 접수 창구 별 소요 시간
    repair_times = list(map(int, input().split()))  # 정비 창구 별 소요 시간
    customer_arrival_times = list(map(int, input().split()))  # 각 고객 도착 시간

    # 접수 창구 상태 관리
    reception_end_time = [0] * N  # 각 접수 창구의 끝나는 시간
    repair_end_time = [0] * M  # 각 정비 창구의 끝나는 시간
    customer_info = []  # 고객별 정보 저장 (고객 번호, 접수 창구, 접수 완료 시간)

    # **Step 1: 접수 창구 배정**
    for customer_id in range(K):  # 각 고객에 대해 접수 창구 탐색
        arrival_time = customer_arrival_times[customer_id]

        # 가장 빨리 사용 가능한 접수 창구 찾기
        best_desk = -1
        best_end_time = float('inf')  # 현재까지 찾은 창구 중 가장 빨리 끝나는 시간

        for desk_id in range(N):
            if reception_end_time[desk_id] <= arrival_time:
                # 즉시 사용할 수 있는 창구 발견
                best_desk = desk_id
                break  # 바로 배정 가능하면 탐색 중단
            elif reception_end_time[desk_id] < best_end_time:
                # 더 빨리 비는 창구를 찾으면 갱신
                best_end_time = reception_end_time[desk_id]
                best_desk = desk_id

        # 고객을 해당 창구에 배정
        if reception_end_time[best_desk] <= arrival_time:
            reception_end_time[best_desk] = arrival_time + reception_times[best_desk]
        else:
            reception_end_time[best_desk] += reception_times[best_desk]

        customer_info.append((customer_id, best_desk, reception_end_time[best_desk]))

    # 접수 완료된 고객을 정비 순서대로 정렬 (접수 완료 시간 기준)
    customer_info.sort(key=lambda x: (x[2], x[1]))

    # **Step 2: 정비 창구 배정**
    final_customer_info = []  # 최종 (고객 번호, 접수 창구 번호, 정비 창구 번호) 저장

    for customer_id, reception_desk, reception_finish_time in customer_info:
        # 가장 빨리 사용 가능한 정비 창구 찾기
        best_repair_desk = -1
        best_end_time = float('inf')

        for repair_desk_id in range(M):
            if repair_end_time[repair_desk_id] <= reception_finish_time:
                # 즉시 사용할 수 있는 정비 창구 발견
                best_repair_desk = repair_desk_id
                break
            elif repair_end_time[repair_desk_id] < best_end_time:
                best_end_time = repair_end_time[repair_desk_id]
                best_repair_desk = repair_desk_id

        # 고객을 정비 창구에 배정
        if repair_end_time[best_repair_desk] <= reception_finish_time:
            repair_end_time[best_repair_desk] = reception_finish_time + repair_times[best_repair_desk]
        else:
            repair_end_time[best_repair_desk] += repair_times[best_repair_desk]

        final_customer_info.append((customer_id, reception_desk, best_repair_desk))

    # **Step 3: 결과 계산**
    result = sum(cust_id + 1 for cust_id, rec_desk, rep_desk in final_customer_info if rec_desk == A and rep_desk == B)

    if result == 0:
        result = -1  # 조건을 만족하는 고객이 없으면 -1 출력

    print(f'#{tc} {result}')
