import sys
from collections import deque
sys.stdin = open('sample_input.txt')

"""
이번 문제는 bfs가 더 좋다고 한다. dfs로 풀면 잘 안되는 부분이 있다고 하니, dfs로 풀면 왜 안되는지 gpt한테 물어보자

끝나고 dfs, bfs를 정리해보자 -> 언제 쓰면 좋을지 판단해보기 -> gpt한테 물어보기

1. 시간당 1의 거리를 움직일 수 있다.
2. 터널은 7종류 터널 구조물로 이루어져있다.
3. 첫번쨰: 상하좌우, 두번쨰: 상하, 세번째: 좌,우, 네번쨰: 상,우, 다섯번쨰: 하, 우, 여섯번째: 하, 좌, 일곱번째: 상, 좌
4.  한시간 뒤에 들어감 -> 맨홀에서 시작 1시간부터 2시간부터 움직인 것으로 보면 됨

출력
탈주범이 있을 수 있는 위치 -> 안움직일 수도 있다? -> 그냥 지나갈 수 있는 모든 지점이 정답에 포함되어야 한다. 
"""
# 상하좌우
dx = (-1,1,0,0)
dy = (0,0,-1,1)


def find_num(t_type):
    list_num = []
    if t_type == 1:
        list_num = [0,1,2,3]
    elif t_type == 2:
        list_num = [0, 1]
    elif t_type == 3:
        list_num = [2, 3]
    elif t_type == 4:
        list_num = [0, 3]
    elif t_type == 5:
        list_num = [1, 3]
    elif t_type == 6:
        list_num = [1, 2]
    elif t_type == 7:
        list_num = [0, 2]
    return list_num


def bfs():
    global map_arr,visited,L, result
    queue = deque([(R,C,L-1)])
    visited[R][C] = 1
    result += 1

    while queue:
        x, y, t= queue.popleft()
        list_num = find_num(map_arr[x][y])

        if t <= 0:
            continue

        for i in list_num:
            nx,ny = x+dx[i], y+dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                list_num_after = find_num(map_arr[nx][ny])
                if visited[nx][ny] == 0 and i == 0 and 1 in list_num_after:
                    visited[nx][ny] = 1
                    queue.append((nx, ny, t - 1))
                    result += 1


                elif visited[nx][ny] == 0 and i == 1 and 0 in list_num_after:
                    visited[nx][ny] = 1
                    queue.append((nx, ny, t - 1))
                    result += 1


                elif visited[nx][ny] == 0 and i == 2    and 3 in list_num_after:
                    visited[nx][ny] = 1
                    queue.append((nx, ny, t - 1))
                    result += 1


                elif visited[nx][ny] == 0 and i == 3 and 2 in list_num_after:
                    visited[nx][ny] = 1
                    queue.append((nx, ny, t - 1))
                    result += 1

T = int(input())

for test_case in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    map_arr = [list(map(int,input().split())) for _ in range(N)]
    visited = [list([0]*M) for _ in range(N)]
    result = 0
    bfs()
    print("#%d %d"%(test_case, result))

