import sys
sys.stdin = open("sample_input.txt", "r")

def inspect(film,K):
    for i in range(W):
        stack = 0
        for j in range(D-1):
            if film[j][i] == film[j+1][i]:
                stack += 1
            else :
                stack = 0
            # K 개 연속 보장 -> 더 이상 검사할 필요 없음
            if stack == K-1 :
                break
        # 한 줄이라도 만족 못하면 이거는 잘못 된 것
        if stack != K-1 :
            return False
    return True

# L : 현재까지 바른 약품 개수, s : 다음에 선택할 행의 인덱스, flim : 현재 상태의 필름 (2D 리스트)
def dfs(L,s,film):
    global answer

    # 최소 조건을 찾아야 해서 큰 갯수는 전부 무시 해도 됨
    if L >= answer:
        return

    # inspect 검사 했을 때 얘가 통과 했을 때 진행 하게 하기
    if inspect(film,K):
        # L이 더 작을 때 L을 업데이트
        if L < answer:
            answer = L
        return

    # 불필요한 연산이라서 종료한다. 연속된 K개에 약을 바르면, 무조건 조건 만족하니까
    if L == K:
        if L < answer:
            answer = L
        return

    # 아니라면?
    else :
        for i in range(s,D):
            switched = []
            for j in range(W):
                if film[i][j] == 1:
                    film[i][j] = 0
                    switched.append(j)
            dfs(L+1, i+1, film)

            #백 트레킹, 재귀가 끊어지면 다시 원복 해야됨, 겁나 어렵네..
            for j in switched:
                film[i][j] = 1

            switched = []
            for j in range(W):
                if film[i][j] == 0:
                    film[i][j] = 1
                    switched.append(j)
            dfs(L+1, i+1, film)
            for j in switched:
                film[i][j] = 0

# 보호 필름의 두께 D, 가로크기 W, 합격기준 K
T = int(input())
for t in range(1,1+T):

    D, W, K = map(int, input().split())
    films = [list(map(int, input().split())) for _ in range(D)]
    answer = 1000000
    if K == 1:
        print(f'#{t} {0}')
    else :
        dfs(0,0,films)
        print(f'#{t} {answer}')

