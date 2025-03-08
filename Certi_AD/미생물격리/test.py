import sys
from collections import deque

sys.stdin = open('sample_input.txt')
T = int(input())

# 상,하,좌,우
dx = (-1,1,0,0)
dy = (0,0,-1,1)

def check_combine(new_arr):
    coord_dict = {}

    for x, y, num, direction in new_arr:
        if (x, y) not in coord_dict:
            coord_dict[(x, y)] = [x, y, num, direction, num]  # (x, y, sum_num, direction, max_num)
        else:
            coord_dict[(x, y)][2] += num  # 미생물 수 합산
            if num > coord_dict[(x, y)][4]:  # 가장 큰 num을 가진 direction 유지
                coord_dict[(x, y)][3] = direction
                coord_dict[(x, y)][4] = num  # max_num 업데이트

    # **num == 0 인 경우 최종적으로 필터링**
    return deque([ [x, y, total_num, direction] for x, y, total_num, direction, _ in coord_dict.values() if total_num > 0 ])

def calculate_results(array):
    global M, K
    new_arr = deque(array.copy())
    now_time = 0

    while now_time < M:
        len_arr = len(new_arr)
        for i in range(len_arr):
            x, y, num, direction = new_arr.popleft()

            # 다음 칸으로 이동
            new_x = x + dx[direction - 1]
            new_y = y + dy[direction - 1]

            # 약 칠해진 곳에 닿으면 방향 반전 및 미생물 감소
            if new_x == 0 or new_x == N-1 or new_y == 0 or new_y == N-1:
                new_direction = direction % 2 + (direction // 3) * 2 + 1
                new_num = num // 2  # 소수점 버림
            else:
                new_direction = direction
                new_num = num

            # **new_num == 0이면 절대 추가 안 되도록 보장**
            if new_num > 0:
                new_arr.append([new_x, new_y, new_num, new_direction])

        # 같은 좌표의 미생물 합치기
        new_arr = check_combine(new_arr)

        now_time += 1

    # 최종 결과 계산
    return sum(num for x, y, num, direction in new_arr)


# 입력 및 실행
for test_case in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(K)]

    results = calculate_results(arr)
    print("#%d %d" % (test_case, results))
