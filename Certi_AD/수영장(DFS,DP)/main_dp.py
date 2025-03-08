import sys

sys.stdin = open('sample_input.txt')

def solve():
    global one_day, one_month, three_month, year, plan

    # DP 테이블 초기화 (0~12월까지)
    dp = [0] * 13

    for i in range(1, 13):  # 1월부터 12월까지 계산
        # 1일권 사용
        dp[i] = dp[i-1] + plan[i-1] * one_day

        # 1달권 사용
        dp[i] = min(dp[i], dp[i-1] + one_month)

        # 3달권 사용 (3개월 이상일 때만 가능)
        if i >= 3:
            dp[i] = min(dp[i], dp[i-3] + three_month)

    # 1년권 사용
    dp[12] = min(dp[12], year)

    return dp[12]


T = int(input())

for test_case in range(1, T + 1):
    one_day, one_month, three_month, year = map(int, input().split())
    plan = list(map(int, input().split()))  # 1월~12월까지 수영장(DFS,DP) 이용 계획
    result = solve()
    print(f"#{test_case} {result}")
