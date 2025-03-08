import sys
"""
주어진 것
1. 1 -> 사람, 1 이상 숫자 -> 계단, 그 숫자가 계단 내려가는데 걸리는 시간
2. 계단 입구까지 이동시간은 절대값으로 계산 식이 주어져있음
3. 계단 각각에 사람들이 갔을 때 최소 시간을 dfs로 풀면 될듯
4. 계단 입구에 도착하면 1분 후 아래칸으로 이동 가능
5. 계단에 3명까지가 최대 인원임

접근 방식
1. dfs로 각각의 사람들이 어떤 계단에 갔을 때 이동 완료 시간이 최소가 되게 하는 시간
2. 종료 조건: 모든 사람이 다 내려 갔을 때 -> 인원 대기 리스트가 다 비었을 때
3. 


찾아봐야 할 것
1. dp가 무엇인가? 시뮬레이션이 무엇인가? -> 다 까먹은듯
"""

import itertools
sys.stdin = open('sample_input.txt')
T = int(input())
for test_case in range(1, 2):
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    person_dict = {}
    stair_dict = {}
    for row in range(N):
        for column in range(N):
            if board[row][column] == 0:
                continue
            elif board[row][column] == 1:
                person_dict[(row,column)] = True
            else:
                stair_dict[(row,column)] = board[row][column]


    stair_time = list(stair_dict.values())

    time_dict = {}
    for person in person_dict:
        temp = []
        for stair in stair_dict:
            temp.append(abs(person[0]-stair[0])+abs(person[1]-stair[1])+1)
        time_dict[person] = temp
    min_time = 1e6
    for stair in list(itertools.product([0,1], repeat = len(person_dict))):
        #print('이용할 계단 : ', stair)
        # 사람 좌표: 걸리는 시간
        first_stair = {}
        second_stair = {}
        for num,person in enumerate(person_dict):
            if stair[num] == 0:
                first_stair[person] = time_dict[person][0]
            elif stair[num] == 1:
                second_stair[person] = time_dict[person][1]
        first_stair_time = sorted(list(first_stair.values()))
        second_stair_time = sorted(list(second_stair.values()))
        print('첫번쨰 계단 이용 시간 : ', first_stair_time)
        print('두번째 계단 이용 시간 : ', second_stair_time)

        first_time = 0
        first_stair_use = []
        print("stair time",stair_time)
        for num in range(len(first_stair_time)):
            if len(first_stair_use) == 3:
                first_time = first_stair_use.pop(0) + stair_time[0]  # 가장 오래된 사람 제거
            time = first_stair_time[num]
            print("time", time)
            first_time = max(first_time, time)  # 현재 사람이 계단을 이용할 수 있는 시간 조정
            print("first time", first_time)
            first_stair_use.append(first_time)  # 현재 사람 추가
            print("first_stair_use", first_stair_use)

        #마지막 사람이 계단 다 내려갈 때
        first_time += stair_time[0]

        print("first_time",first_time)
        second_time = 0
        second_stair_use = []
        for num in range(len(second_stair_time)):
            if len(second_stair_use) == 3:
                second_time = second_stair_use[0]+ stair_time[1]
                second_stair_use = second_stair_use[2-second_stair_use[::-1].index(second_stair_use[0])+1:]
            time = second_stair_time[num]

            if second_time <time:
                second_time = time
            second_stair_use.append(second_time)
        second_time += stair_time[1]
        min_time = min(min_time, max(first_time,second_time))
    print("#%d %d"%(test_case,min_time))







