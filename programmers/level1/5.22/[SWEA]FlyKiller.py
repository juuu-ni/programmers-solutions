T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(N)]
     
    mx = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            ret = 0
            for k in range(i, i + M):
                for l in range(j, j + M):
                    ret += array[k][l]
            mx = max(mx, ret)
     
    print(f"#{test_case} {mx}")