T = int(input())
for i in range(1,T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]

    dr = [0,1,0,-1]
    dc = [1,0,-1,0]
    r,c,d,=0,0,0

    for num in range(1,N*N+1):
        arr[r][c]=num
        nr,nc = r+ dr[d], c+dc[d]
        if nr<0 or nr>=N or nc<0 or nc>=N or arr[nr][nc]!=0:
            d=(d+1)%4
            nr,nc = r+dr[d], c+dc[d]
        r,c=nr,nc
    print(f'#{i}')
    for row in arr:
        print(*row)