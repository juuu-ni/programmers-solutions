T = int(input())
for t in range(1,T+1):
    lst = list(map(int,input().split()))
    sum_odd = sum(i for i in lst if i%2!=0)
    print(f'#{t}', sum_odd)