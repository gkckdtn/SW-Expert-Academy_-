import sys
sys.stdin = open("sample_input.txt", "r")
T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    atom = [list(map(int,input().split())) for _ in range(n)]
    # 상하좌우 배열
    dir = [(0,0.5),(0,-0.5),(-0.5,0),(0.5,0)]
    result = 0
    while len(atom)>=2:
        for i in range(len(atom)):
            # 방향에 따라 모든 atom x,y 좌표 업데이트
            atom[i][0] += dir[atom[i][2]][0]
            atom[i][1] += dir[atom[i][2]][1]
        location = {}
        for a in atom:
            try:
                location[(a[0],a[1])].append(a)
            except:
                location[(a[0],a[1])] = [a]
        atom = []
        for i in location:
            if len(location[i]) >=2:
                for score in location[i]:
                    result += score[3]
            else:
                if -1000<=location[i][0][0] <=1000 and -1000<= location[i][0][1] <=1000:
                    atom.append(location[i][0])
    print('#%d %d'%(test_case,result))