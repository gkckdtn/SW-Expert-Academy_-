import itertools
import sys

sys.stdin = open('sample_input.txt')
T = int(input())

def calculate_stair_time(stair_time, stair_arrival_times):
    """ 특정 계단에 대해 사람들이 내려가는 최소 시간을 계산 """
    if not stair_arrival_times:
        return 0

    stair_arrival_times.sort()  # 계단에 도착하는 시간 정렬
    stair_queue = []  # 계단을 사용 중인 사람들의 종료 시간
    stair_complete_time = 0

    for arrival_time in stair_arrival_times:

        print("arrival_time", arrival_time)
        if len(stair_queue) == 3:  # 계단이 가득 차 있으면, 가장 먼저 내려간 사람 제거
            stair_complete_time = stair_queue.pop(0)
        print("stair_complete_time", stair_complete_time)
        start_time = max(stair_complete_time, arrival_time)  # 계단을 이용할 수 있는 시간 계산
        finish_time = start_time + stair_time  # 계단을 완전히 내려가는 시간
        stair_queue.append(finish_time)  # 계단 사용 종료 시간 저장
        print("stair_queue",stair_queue)
    return stair_queue[-1]  # 마지막 사람이 내려가는 시간 반환

for test_case in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    people = []  # 사람들의 위치
    stairs = []  # 계단의 위치 및 내려가는 시간

    # 입력 처리: 사람과 계단의 위치 저장
    for r in range(N):
        for c in range(N):
            if board[r][c] == 1:
                people.append((r, c))
            elif board[r][c] > 1:
                stairs.append((r, c, board[r][c]))  # (행, 열, 내려가는 시간)

    min_total_time = float('inf')

    # 모든 사람에 대해 계단 선택 경우의 수를 고려
    for stair_choice in itertools.product([0, 1], repeat=len(people)):
        #print("stair_choice",stair_choice)
        first_stair_times = []  # 첫 번째 계단을 선택한 사람들의 도착 시간
        second_stair_times = []  # 두 번째 계단을 선택한 사람들의 도착 시간

        for i, (r, c) in enumerate(people):
            stair_idx = stair_choice[i]  # 이 사람이 선택한 계단 (0 또는 1)
            stair_r, stair_c, stair_t = stairs[stair_idx]
            arrival_time = abs(r - stair_r) + abs(c - stair_c) + 1  # 계단까지 이동 시간 +1분
            if stair_idx == 0:
                first_stair_times.append(arrival_time)
            else:
                second_stair_times.append(arrival_time)

        # 각 계단에서 최소 시간 계산
        first_time = calculate_stair_time(stairs[0][2], first_stair_times)
        second_time = calculate_stair_time(stairs[1][2], second_stair_times)

        # 두 계단을 이용하는 사람이 모두 내려가는 최소 시간 중 최댓값
        total_time = max(first_time, second_time)
        min_total_time = min(min_total_time, total_time)

    print(f"#{test_case} {min_total_time}")
