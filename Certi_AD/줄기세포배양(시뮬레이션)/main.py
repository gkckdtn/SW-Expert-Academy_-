import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

for test_case in range(1, T+1):
    n, m, k = map(int, input().split())
    time = 0
    myMap = [[None] * (m + k) for i in range(n + k)]

    for i in range(n):
        tmp = list(map(int, input().split()))
        for j in range(len(tmp)):
            myMap[i + k // 2][j + k // 2] = tmp[j]

    # 상,우,하,좌
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]


    # active에 활성화된 세포들을 넣기
    active = [[] for i in range(11)]
    for i in range(n + k):
        for j in range(m + k):
            if myMap[i][j]:
                # 만약 활성화된 세포가 있으면
                active[myMap[i][j]].append([i, j, myMap[i][j]])
                # active에 position 정보와 세포의 hp 정보를 append
    #print(active)
    # k만큼 지남
    for i in range(k):
        for power in range(10, 0, -1):
            # 생명력이 가장 큰 것 부터 번식 시작
            cells = active[power]

            # 이번 시간에 번식된 세포들을 저장
            new = []
            # 이번 시간에 죽은 세포들 저장
            old = []
            for j in range(len(cells) - 1, -1, -1):

                cells[j][2] -= 1
                # hp를 감소시킴
                x, y, hp = cells[j]
                #print("cells", cells)
                if hp == -1:
                    # hp가 + 상태면 비활성화이고, -상태이면 활성화 시작
                    # 활성화를 하면서 번식 시작
                    for dir in range(4):
                        cx = x + dx[dir]
                        cy = y + dy[dir]
                        if (not myMap[cx][cy]):
                            # 만약 다음 공간이 빈 공간이면
                            myMap[cx][cy] = power
                            new.append([cx, cy, power])
                            # 번식을 하고, 번식된 세포의 정보를 new에 저장
                if hp == -power:
                    # 만약 활성화 최대 hp에 도달하면
                    old.append(j)
                    #print('old', old)
                    # 죽은 세포로 간주해서 old에 저장

            for idx in old:
                # 해당 우선순위(높은 hp)의 번식, 활성화가 끝났으면
                # old에 있는 cells를 버리기
                cells.pop(idx)
                #print("pop",cells)
            cells += new
            #print("new",new)
            # call of reference(함수 호출 방식)
            # active[power] += new로 해도 괜찮음
            # 번식된 최신 세포의 정보를 cells에 저장
        #print("active",active)
    result = 0
    for i in range(1, 11):
        result += len(active[i])
    print("#{} {}".format(test_case, result))