import sys
from operator import contains

sys.stdin = open('sample_input.txt')

"""
1. 1일 이용권: 1일 이용 가능
2. 1달 이용권: 1달 이용 가능
3. 3달 이용권: 연속된 3달 동안 이용 가능, 3달 이용권은 매달 1일부터 시작
- 11월 12월에도 3달 이용권 사용 가능, 11,12,1 이렇게는 안됨
4. 1년 이용권: 1년동안 이용 가능, 매년 1월 1일부터 시작

요금, 각 달 이용계획 입력 -> 가장 작은 비용으로 수영장(DFS,DP) 이용 가능 방법 찾기
-> 출력은 그 비용을 정답으로

접근 방식
1. 요금제 별로 써본다. plan list에서 1월달 부터 하나씩 없애나간다.
2. 하나까고 없으면 다음달로 넘어감, 한 달마다 생각해야한다.

12월달까지 가면 return

"""
def dfs(month, month_fee, result):
    global plan_list, min_result
    #print(month, month_fee)
    result += month_fee
    #print(month, month_fee)
    #print("result", result)
    #print("######################################################")

    if month >= 13:
        if result < min_result:
            min_result = result
            #print(month, month_fee)
            #print("min result", result)
            #print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        return


    dfs(month+1, one_day*plan_list[month], result)
    if plan_list[month] != 0:
        decide_fee = 1
    else:
        decide_fee = 0
    dfs(month+1, one_month*decide_fee, result)
    try:
        if plan_list[month] != 0 or plan_list[month+1] != 0 or plan_list[month+2] != 0:
            decide_fee = 1
        else:
            decide_fee = 0
    except:
        if plan_list[month] != 0:
            decide_fee = 1
        else:
            decide_fee = 0
    dfs(month+3, three_month*decide_fee, result)

    dfs(month+12, year, result)


T = int(input())

for test_case in range(1, T+1):
    one_day,one_month,three_month,year = map(int,input().split())
    a = list(map(int,input().split()))
    plan_list = [0]
    for i in a:
        plan_list.append(i)

    # visited = [0*len(plan_list)]
    result = 0
    month = 0
    min_result = 1e9
    dfs(month, 0,result)
    print("#%d %d"%(test_case, min_result))