import sys

sys.stdin = open('sample_input.txt')

def dfs(month, total_cost):
    global min_cost

    # 가지치기 (Pruning): 현재 비용이 최소 비용보다 크면 중단
    if total_cost >= min_cost:
        return

    # 12개월이 지나면 최소 비용 업데이트
    if month >= 12:
        min_cost = min(min_cost, total_cost)
        return

    # 1일 이용권
    dfs(month + 1, total_cost + plan[month] * one_day)

    # 1달 이용권
    dfs(month + 1, total_cost + one_month)

    # 3달 이용권 (현재 달 포함 연속 3개월 사용 가능)
    dfs(month + 3, total_cost + three_month)

    # 1년 이용권 (무조건 연간 패스로 넘어감)
    dfs(12, total_cost + year)


T = int(input())

for test_case in range(1, T + 1):
    one_day, one_month, three_month, year = map(int, input().split())
    plan = list(map(int, input().split()))  # 기존 리스트 그대로 사용
    min_cost = float('inf')  # 최소 비용 초기화

    dfs(0, 0)  # DFS 탐색 시작

    print(f"#{test_case} {min_cost}")
