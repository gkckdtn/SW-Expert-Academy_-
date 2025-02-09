import sys

sys.stdin = open("sample_input.txt", "r")
T = int(input())

for test_case in range(1, T + 1):
    n,K = map(int,input().split())
    num_list = list(map(str,input()))
    cnt = n//4
    arr = []
    for i in range(cnt):
        pop_num = num_list.pop()
        num_list.insert(0,pop_num) # 여기서 deque 사용가능할듯?
        for j in range(0,n,cnt):
            a = ''
            for k in range(j,j+cnt):
                a += num_list[k]
            arr.append(a)
    new_arr = list(set(arr))
    answer = []
    for num in new_arr:
        answer.append(int(num,16))
    sorted_answer = sorted(answer,reverse=True)
    print('#%d %d'%(test_case,sorted_answer[K-1]))
