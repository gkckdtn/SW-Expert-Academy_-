import sys
sys.stdin = open("sample_input.txt", "r")

def dfs(idx, result):
    # print("new dfs")
    global max_num
    global min_num
    if idx == N - 1:  # 연산은 주어진 숫자보다 1번 적으므로 N-1까지 탐색
        # print("----------------------------------------------------------------------------------------")
        # print("end of dfs")
        if max_num <= result:
            max_num = result
        if result <= min_num:
            min_num = result
        # print("max_num",max_num)
        # print("min_num",min_num)
        # print("----------------------------------------------------------------------------------------")
        return

    for i in range(4):  # 연산 4번 만큼 반복
        # print("start_for")
        #연산자가 -1씩 돼서 없어져버림
        if moderator[i] > 0:  # 연산자가 존재한다면
            # print("i print", i)
            # print("base num",result)
            # print("operate num",number[idx + 1])
            #
            # print(mo[i])
            moderator[i] -= 1  # 해당 연산자를 한번 사용한다는 뜻
            # print("moderator", moderator)

            if i == 0:
                new_result = result + number[idx + 1]
            elif i == 1:
                new_result = result - number[idx + 1]
            elif i == 2:
                new_result = result * number[idx + 1]
            else:  # 나눗셈의 경우 음수 나눗셈 때문에 주의가 필요함. int형을 통해 버림을 취함
                new_result = int(result / number[idx + 1])
            # print("idx print, inside", idx)
            # print("----------------------------------------------------------------------------------------")
            dfs(idx + 1, new_result) #끝까지 탐색 -> 모든 경우의 수 다 찾을 수 있음

            moderator[i] += 1
            # 그냥 DFS인데 존재 하는지 아닌지만 파악하고 원복 해주는거 끝까지 가기는 끝까지 간다.
            # print("moderator",moderator)
            # print("idx print, back tracking",idx)


T = int(input())
for t in range(T):
    N = int(input())
    moderator = list(map(int, input().split()))  # [+ - * /]순으로 저장
    mo = ['+','-','*','/']
    number = list(map(int, input().split()))
    max_num = -1e9
    min_num = 1e9
    dfs(0, number[0])
    print('#{} {}'.format(t + 1, max_num - min_num))