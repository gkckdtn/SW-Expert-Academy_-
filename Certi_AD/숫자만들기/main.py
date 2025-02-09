def dfs(idx, result):
    global max_num
    global min_num
    if idx == N - 1:  # 연산은 주어진 숫자보다 1번 적으므로 N-1까지 탐색
        if max_num <= result:
            max_num = result
        if result <= min_num:
            min_num = result
        return

    for i in range(4):  # 연산 4번 만큼 반복
        if moderator[i] > 0:  # 연산자가 존재한다면
            moderator[i] -= 1  # 해당 연산자를 한번 사용한다는 뜻
            if i == 0:
                new_result = result + number[idx + 1]
            elif i == 1:
                new_result = result - number[idx + 1]
            elif i == 2:
                new_result = result * number[idx + 1]
            else:  # 나눗셈의 경우 음수 나눗셈 때문에 주의가 필요함. int형을 통해 버림을 취함
                new_result = int(result / number[idx + 1])
            dfs(idx + 1, new_result)
            moderator[i] += 1


T = int(input())
for t in range(T):
    N = int(input())
    moderator = list(map(int, input().split()))  # [+ - * /]순으로 저장
    number = list(map(int, input().split()))
    max_num = -9999990
    min_num = 99999999
    dfs(0, number[0])
    print('#{} {}'.format(t + 1, max_num - min_num))