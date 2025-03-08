import sys
from copy import deepcopy
from itertools import combinations
import copy
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

# 조합 사용하는 방법 찾아보기 -> 문제 다 풀고
def split_into_two_groups():
    global people_list, stair_list
    n = len(people_list)
    unique_splits = []
    unique_splits_opposite = []

    for i in range(1, n // 2 + 1):  # i개의 원소를 가진 첫 번째 집합 선택
        for group1 in combinations(people_list, i):
            group1 = list(group1)
            group2 = [item for item in people_list if item not in group1]  # 나머지 원소들
            split = [group1, group2]
            group2 = deepcopy(group2)
            group1 = deepcopy(group1)
            split_opposite = [group2, group1]
            if split not in unique_splits and [group2, group1] not in unique_splits:
                unique_splits.append(split)  # 집단이 구분되지 않도록 중복 제거
                unique_splits_opposite.append(split_opposite)

    if len(unique_splits) == 0:
        unique_splits.append([[people_list[0]]])

    return unique_splits, unique_splits_opposite

def dfs():
    global stair_list
    unique_splits, unique_splits_opposite = split_into_two_groups()
    if len(unique_splits_opposite) > 0:
        total_people = unique_splits + unique_splits_opposite
    else:
        total_people = unique_splits
    # stair 1 + stair 2 한 묶음으로 생각 해야 할 듯
    for i in range(len(total_people)):
        #print(total_people[i][0],"aaaaaaaaaa",total_people[i][1])
        for j in range(len(total_people[i][0])):
            time_to_stair_1 = abs(total_people[i][0][j][0] - stair_list[0][0]) + abs(
                total_people[i][0][j][1] - stair_list[0][1])


            total_people[i][0][j] = total_people[i][0][j]+[time_to_stair_1]  # 값 추가
        #
        for k in range(len(total_people[i][1])):
            time_to_stair_2 = abs(total_people[i][1][k][0] - stair_list[1][0]) + abs(
                total_people[i][1][k][1] - stair_list[1][1])

            total_people[i][1][k] = total_people[i][1][k] + [time_to_stair_2]  # 값 추가!!!!!!!!!!!!!! 이걸로 추가하기ㅣㅣㅣㅣ

    print(total_people)  # 변경 후 출력

    # 이제 차례 대로 돌면서 시간을 반환 해주면 됨
    for num in range(len(total_people)):
        now_people_list = deepcopy(total_people[num])
        now_time = 0
        stair_1_now = []
        while now_time < 10:
            for num_1 in range(len(now_people_list[0])):

                if now_time == now_people_list[0][num_1][2]:
                    stair_1_now.append(now_people_list[0][num_1])
                    del now_people_list[0][num_1]
                    print(stair_1_now)
            for num_2 in now_people_list[1]:
                if now_time == num_2[2]:
                    print("now")



            now_time += 1


    # 하나만 있는 경우는 따로 생각해주자



sys.stdin = open('sample_input.txt')
T = int(input())

for test_case in range(1, 2):
    N = int(input())
    map_stair = list(list(map(int, input().split())) for _ in range(N))
    people_list = []
    stair_list = []
    for i in range(N):
        for j in range(N):
            # 사람 있는 위치 알아내기
            if map_stair[i][j] == 1:
                people_list.append([i,j])
            elif map_stair[i][j] > 1:
                stair_list.append([i,j,map_stair[i][j]])
    #print(people_list,stair_list)
    #a,b = split_into_two_groups()
    #print(a)
    #print(a[0][0])
    dfs()
    results = 0

    print("#%d %d"%(test_case,results))
