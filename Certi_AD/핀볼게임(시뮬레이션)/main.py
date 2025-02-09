import sys
sys.stdin = open("sample_input.txt", "r")
T = int(input())

# 1~4번 삼각형
# 1번: 오른쪽 -> 왼쪽 , 위쪽 -> 아래쪽
# 5번 정사각형
# 6~10 웜홀
# -1 블랙홀

'''
1. 방향 이동 정의
- 공은 위(0), 오른쪽(1), 아래(2), 왼쪽(3) 네 방향으로 이동할 수 있습니다.
directions 리스트를 사용하여 방향 이동을 쉽게 처리합니다.

2. 블록 충돌 처리
- 5가지 블록(1~5번)이 있으며, 블록을 만나면 정해진 방향으로 튕깁니다. blocks 리스트를 사용하여 방향을 변환할 수 있도록 설정합니다.

3. 웜홀 이동 처리
- 같은 숫자의 웜홀(6~10번) 두 개가 서로 연결되어 있습니다. 웜홀에 도착하면 반대편 웜홀로 이동합니다.

4. 게임 종료 조건
- 벽에 부딪히거나 블랙홀(-1)을 만나거나 출발점으로 돌아오면 종료됩니다.
'''

#판 나왔을 때 위치 이동은 이렇게 하면 됨
directions = [(-1,0),(0,1),(1,0),(0,-1)] # 위, 오른쪽, 아래, 왼쪽

# 위, 오른, 아래, 왼 순으로 인덱싱 할 수 있다.
blocks = [
    [], #블록 0번
    [2,3,1,0], #블록 1번 위 -> 아래, 오른 -> 왼, 아래 -> 오른, 왼 -> 위
    [1,3,0,2], #블록 2번
    [3,2,0,1], #블록 3번
    [2,0,3,1], #블록 4번
    [2,3,0,1] #블록 5번
]

#게임판 범위 검사
def check(x,y):
    if 0 <= x < n and 0<=y <n:
        return True
    return False

def get_score(start_x, start_y,start_dir):
    dx,dy,dir = start_x,start_y,start_dir
    score = 0
    while True:
        # 방향에 따라서
        dx = dx + directions[dir][0]
        dy = dy + directions[dir][1]
        if check(dx,dy):

            # 삼각형부터 정사각형일 때
            if data[dx][dy] in range(1,6):
                block_type = data[dx][dy]
                score +=1
                dir = blocks[block_type][dir]
                continue

            # 웜홀 만났을 때
            elif data[dx][dy] in range(6,11):
                hall_type = data[dx][dy]

                # 두개의 쌍 중에 하나에 만났을 떄
                if (dx,dy) == wormhole[hall_type][0]:
                    dx,dy = wormhole[hall_type][1]

                # 두개의 쌍 중에 다른 하나에 만났을 때
                elif (dx,dy) == wormhole[hall_type][1]:
                    dx,dy = wormhole[hall_type][0]
                continue

            # 블랙홀 만났을 때
            elif data[dx][dy] == -1:
                return score

            # 처음 시작 지점 도달
            elif (dx,dy) == (start_x,start_y):
                return score
            # 빈공간일 때
            else:
                continue
        else:
            dir = (dir+2) %4 # 이 스킬 정말 맘에 든다 반대 방향 나머지로 2칸씩 당기는 것.
            score += 1

for tc in range(1, T + 1):
    n = int(input())
    data = [list(map(int,input().split())) for _ in range(n)]
    print(data)
    result = 0
    wormhole = [[]for _ in range(11)]
    for i in range(n):
        for j in range(n):
            value = data[i][j]
            if value in range(6, 11):  # 웜홀일 경우
                wormhole[value].append((i, j))  # 좌표 삽입

    for i in range(n):
        for j in range(n):
            if data[i][j] == 0:
                for k in range(4):
                    score = get_score(i,j,k)
                    result = max(result,score)
    print('#%d %d' %(tc,result))
# a = 0.12345
# print('%.02f'%(a))
