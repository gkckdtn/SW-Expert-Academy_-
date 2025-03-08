import sys
from collections import deque
'''
1. 접수 창구 개수: N
2. 정비 창구 개수: M
3. 차량 정비소 방문 고객 수 K
4. 지갑 두고간 고객 접수 창구 A, 정비 창구 B
5. 접수 창구 소요 시간, ai, 정비 창구 소요 시간 bj
6. k 번째 고객 방문 시간 tk

출력 : A,B를 같이 사용한 고객 번호 합

'''
sys.stdin = open('sample_input.txt')
T = int(input())

def find_wallet(tk, visited_a, visited_b, a_i_list, b_j_list):
    waiting_queue = deque([])
    reception_queue = deque([])
    repair_wating_queue = deque([])
    repair_queue = deque([])
    survey_queue = deque([])
    last_time = tk[-1]
    present_time = 0
    list_reception = []
    list_repair = []
    while len(survey_queue) != len(tk): # survey_queue에 보낸 사람이 정원이 다 차면
        # print("present_time", present_time)
        # 현재 시간 진입, 1. 현재 시간에 해당하는 사람 정수 queue에 저장
        # 현재 시간에 맞는 고객 리스트 탐색
        # 이 모든 과정이 0 시간에 일어나야됨
        for i in range(len(tk)):
            if present_time == tk[i]:
                waiting_queue.append((i,present_time))

        #현재 시간에 맞는 고객 큐 추가 완료
        #이제 reception이 비었는지 확인 -> 근데 동시에 진행되어야 함
        if waiting_queue:
            for j in range(len(visited_a)):
                for _ in range(len(waiting_queue)):
                    if visited_a[j] == 0:
                        customer_waiting, time_reception = waiting_queue.popleft()
                        if time_reception <= present_time:
                            #print("popleft waiting_queue",customer_waiting, time_reception)
                            reception_queue.append((customer_waiting, present_time + a_i_list[j], j))
                            visited_a[j] = 1
                            if j == A-1:
                                list_reception.append(customer_waiting)
                        else:
                            waiting_queue.append((customer_waiting, time_reception))
        #print("reception_queue", reception_queue)


        # repair 대기 줄
        if reception_queue:
            for _ in range(len(reception_queue)):
                customer_reception, time_repair, reception_num_before = reception_queue.popleft()
                if time_repair == present_time:
                    repair_wating_queue.append((customer_reception, time_repair, reception_num_before))
                    visited_a[reception_num_before] = 0
                    if waiting_queue:
                        customer_waiting, time_reception = waiting_queue.popleft()
                        if time_reception <= present_time:
                            #print("popleft waiting_queue", customer_waiting, time_reception)
                            reception_queue.append((customer_waiting, present_time + a_i_list[reception_num_before], reception_num_before))
                            visited_a[reception_num_before] = 1
                            if reception_num_before == A - 1:
                                list_reception.append(customer_waiting)
                        else:
                            waiting_queue.append((customer_waiting, time_reception))

                else:
                    reception_queue.append((customer_reception, time_repair, reception_num_before))



        if repair_wating_queue:
            # reception queue에 들어온 사람 추가
            for k in range(len(visited_b)):
                    #print("reception queue pop left",reception_queue.popleft())
                    for _ in range(len(repair_wating_queue)):
                        if visited_b[k] == 0:
                            customer_reception, time_repair, reception_num_before = repair_wating_queue.popleft()
                            if time_repair <= present_time:
                                #print("popleft reception_queue", customer_reception, time_repair, reception_num_before)
                                repair_queue.append((customer_reception, present_time+ b_j_list[k], k))
                                visited_b[k] = 1
                                if k == B-1:
                                    list_repair.append(customer_reception)
                            else:
                                repair_wating_queue.append((customer_reception, time_repair, reception_num_before))

        # print("waiting_queue2", waiting_queue)
        # print("reception_queue2", reception_queue)
        # print("repair_waiting2", repair_wating_queue)
        # print("repair_queue2", repair_queue)


        if repair_queue:
            #print("repair_queue",repair_queue)
            for _ in range(len(repair_queue)):
                customer_repair, time_survey, repair_num_before = repair_queue.popleft()
                if time_survey == present_time:
                    visited_b[repair_num_before] = 0
                    survey_queue.append(customer_repair)

                else:
                    repair_queue.append((customer_repair, time_survey, repair_num_before))

        if repair_wating_queue:
            # reception queue에 들어온 사람 추가
            for k in range(len(visited_b)):
                    #print("reception queue pop left",reception_queue.popleft())
                    for _ in range(len(repair_wating_queue)):
                        if visited_b[k] == 0:
                            customer_reception, time_repair, reception_num_before = repair_wating_queue.popleft()
                            if time_repair <= present_time:
                                #print("popleft reception_queue", customer_reception, time_repair, reception_num_before)
                                repair_queue.append((customer_reception, present_time+ b_j_list[k], k))
                                visited_b[k] = 1
                                if k == B-1:
                                    list_repair.append(customer_reception)
                            else:
                                repair_wating_queue.append((customer_reception, time_repair, reception_num_before))


        # print("waiting_queue3", waiting_queue)
        # print("reception_queue3", reception_queue)
        # print("repair_waiting3", repair_wating_queue)
        # print("repair_queu3", repair_queue)
        # print("survey_queue3",survey_queue)


        present_time += 1
        # print("################################################################")
        # if present_time ==20:
        #     return


    sum_total = 0
    # print(list_reception, list_repair)
    for i in list_reception:
        for k in list_repair:
            if i == k:
                sum_total += (i+1)

    return sum_total


for test_case in range(1, T+1):
    N,M,K,A,B = map(int, input().split())
    a_i_list = list(map(int, input().split()))
    b_j_list = list(map(int, input().split()))
    tk = list(map(int, input().split()))
    result = 0
    visited_a = [0] * N
    visited_b = [0] * M
    sum_total = find_wallet(tk, visited_a, visited_b, a_i_list, b_j_list)
    print("#%d %d"%(test_case,sum_total))

