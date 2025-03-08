import sys

sys.stdin = open('sample_input.txt')

def dfs(month, total_cost):
    global min_result

    # 최소 비용 초과하면 더 탐색할 필요 없음 (가지치기)
    if total_cost >= min_result:
        return

    # 12월 넘어가면 최소 비용 업데이트
    if month >= 12:
        min_result = min(min_result, total_cost)
        return

    # 1일 이용권
    dfs(month + 1, total_cost + one_day * plan_list[month])

    # 1달 이용권
    if plan_list[month]:  # 해당 월에 이용 계획이 있는 경우에만 1달권 고려
        dfs(month + 1, total_cost + one_month)

    # 3달 이용권
    if any(plan_list[month:month+3]):  # 3달 내에 한 번이라도 수영장이용이 있으면
        dfs(month + 3, total_cost + three_month)

    # 1년 이용권
    dfs(12, total_cost + year)  # 바로 1년 치로 넘어감


T = int(input())

for test_case in range(1, T + 1):
    one_day, one_month, three_month, year = map(int, input().split())
    plan_list = list(map(int, input().split()))  # 기존 리스트 그대로 사용
    min_result = float('inf')  # 최소 비용 초기화

    dfs(0, 0)  # 인덱스 0부터 시작
    print(f"#{test_case} {min_result}")
