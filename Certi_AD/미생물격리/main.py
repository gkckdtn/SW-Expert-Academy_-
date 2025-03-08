import sys
from collections import deque
'''
문제 지시 사항
1. 약품이 칠해진 곳에 도달하면 미생물이 반으로 줄고, 이동방향은 반대가 된다. 
2. 홀수 일 때는 2로 나눈 후 소숫점 버림 // 이거 쓰면 됨
3. 합쳐지는데, 합쳐지는 수가 같을 때는 고려 안해도 된다. 합쳐질 때 미생물 수가 많은 방향으로 이동 방향 설정
4. M 시간 동안 미생물 격리, 남아있는 미생물 총 합
5. 1시간 마다 이동방향 한칸 이동

접근 방향
1. 네방향 설정
2. 이동 후 합쳐지는 미생물이 있는지? 미생물 이동 방향을 제일 수가 많은 미생물 이동방향으로 설정
3. 언제 끝나? 시간이 M시간 지났을 때
4. 이거는 그냥 시뮬레이션 문제인 것 같다. 어떤 문제인가 물어보기 
'''
sys.stdin = open('sample_input.txt')
T = int(input())

# 상,하,좌,우
dx = (-1,1,0,0)
dy = (0,0,-1,1)



def check_combine(new_arr):
    coord_dict = {}

    for x,y,num,direction in new_arr:

        if (x,y) not in coord_dict:
            coord_dict[(x, y)] = [x,y,num,num, direction]
        elif (x,y) in coord_dict:
            coord_dict[(x, y)][3] += num
            coord_dict[(x,y)][0] = x
            coord_dict[(x, y)][1] = y
            if coord_dict[(x, y)][2] < num:
                coord_dict[(x, y)][4] = direction
                coord_dict[(x, y)][2] = num #가장 큰거 업데이트 해야됨
    #print(list(coord_dict.values()))
    coord_dict_2 = {}
    for x,y,num,sum_num,direction in list(coord_dict.values()):

        coord_dict_2[(x, y)] = [x, y, sum_num, direction]
    #print(list(coord_dict.values()))
    return deque(list(coord_dict_2.values()))

def calculate_results(array):
    global M,K
    new_arr = deque(array.copy())
    now_time = 0
    #print(new_arr)
    while now_time < M:
        len_arr = len(new_arr)
        for i in range(len_arr):
            x, y, num, direction = new_arr.popleft()
            # 다음 칸으로 현재 방향으로 이동
            #print("before plus",x,y,dx[direction-1], dy[direction-1])
            new_x = x + dx[direction-1]
            new_y = y + dy[direction-1]
            #print("plus",new_x,new_y)

            # 약 칠해진 곳에 닿을 때 방향 반대로 바꿈, 미생물 반 죽음
            if new_x == 0 or new_x== N-1 or new_y == 0 or new_y == N-1:
                new_direction = direction%2 +(direction//3)*2 +1

                #print(new_direction)
                new_num = num//2
            else:
                new_direction = direction
                new_num = num

            # 한마리 남아있을 때 0이 되면 사라짐
            if new_num > 0:
                #print("append",new_x,new_y,new_num,new_direction)
                new_arr.append([new_x, new_y, new_num, new_direction])

        new_arr = check_combine(new_arr)

        now_time += 1
        #print("##############",len(new_arr),result)
    result = 0

    for x,y,num,direction in new_arr:
        print(num)
        result += num
    return result


for test_case in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = []
    for _ in range(K):
        arr.append(list(map(int, input().split())))

    results = calculate_results(arr)
    print("#%d %d"%(test_case,results))