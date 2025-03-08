import sys
from collections import deque

sys.stdin = open('sample_input.txt')

# 상, 하, 좌, 우 (0,1,2,3)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 터널 구조에 따른 이동 가능 방향 (딕셔너리 활용)
TUNNEL_MAP = {
    1: [0, 1, 2, 3],  # 상하좌우
    2: [0, 1],        # 상하
    3: [2, 3],        # 좌우
    4: [0, 3],        # 상우
    5: [1, 3],        # 하우
    6: [1, 2],        # 하좌
    7: [0, 2]         # 상좌
}

# 반대 방향 체크용 (0 <-> 1, 2 <-> 3)
OPPOSITE = {0: 1, 1: 0, 2: 3, 3: 2}

def bfs():
    queue = deque([(R, C, L - 1)])
    visited[R][C] = 1  # 시작 위치 방문 처리
    count = 1  # 초기 위치 포함

    while queue:
        x, y, t = queue.popleft()

        if t == 0:
            continue  # 시간이 0이면 더 이상 이동 불가

        # 현재 터널에서 이동 가능한 방향 확인
        for direction in TUNNEL_MAP[map_arr[x][y]]:
            nx, ny = x + dx[direction], y + dy[direction]

            # 범위 내 & 방문 안한 곳인지 확인
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                # 이동하려는 곳이 터널이고, 해당 방향으로 들어갈 수 있는지 체크
                if map_arr[nx][ny] and OPPOSITE[direction] in TUNNEL_MAP[map_arr[nx][ny]]:
                    visited[nx][ny] = 1  # 방문 처리
                    queue.append((nx, ny, t - 1))
                    count += 1  # 이동 가능 위치 증가

    return count

# 입력 처리
T = int(input())

for test_case in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    map_arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    result = bfs()
    print(f"#{test_case} {result}")
