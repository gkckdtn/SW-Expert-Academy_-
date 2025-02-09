import sys
sys.stdin = open("sample_input.txt", "r")
T = int(input())

#이동x, 상, 우, 하 좌
dx = [0,0,1,0,-1]
dy = [0,-1,0,1,0]

for test_case in range(1, T + 1):

    m, a = map(int,input().split())
    move_a = list(map(int,input().split()))
    move_b = list(map(int, input().split()))

    # 문제에 주어진 판은 1부터 시작하니까 조심해야된다.
    board = [list(map(int, input().split())) for _ in range(a)]
    pos_a = [0,0]
    pos_b = [9,9]
    result = 0
    idx = -1
    while idx < m:
        temp_result = 0
        a_x, a_y = pos_a
        b_x, b_y = pos_b
        for w in range(a):
            bat_x,bat_y,bat_c,bat_p = board[w]
            temp_a = 0
            if abs(bat_x - a_x - 1) + abs(bat_y - a_y - 1) <= bat_c:
                temp_a += bat_p

            for e in range(a):
                e_x,e_y,e_c,e_p = board[e]
                temp_b = 0

                if abs(e_x - b_x - 1) + abs(e_y - b_y - 1) <=e_c:
                    if w==e and temp_a != 0:
                        pass
                    else:
                        temp_b += e_p

                if temp_result < temp_a + temp_b:
                    temp_result = temp_a + temp_b
        idx += 1

        if idx < m:
            pos_a = [pos_a[0]+dx[move_a[idx]],pos_a[1]+dy[move_a[idx]]]
            pos_b = [pos_b[0]+dx[move_b[idx]],pos_b[1]+dy[move_b[idx]]]
        result += temp_result

    print("#%d %d"%(test_case,result))