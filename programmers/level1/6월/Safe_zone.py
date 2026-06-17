def solution(board):
    n = len(board)
    
    danger = [[0] * n for _ in range(n)]
    dr = [-1, 1, 0, 0, -1, -1, 1, 1]
    dc = [0, 0, -1, 1, -1, 1, -1, 1]
    
    for r in range(n):
        for c in range(n):
            if board[r][c] == 1:
                danger[r][c] = 1
                
                
                for i in range(8):
                    nr = r + dr[i] 
                    nc = c + dc[i]
                    
                    
                    if 0 <= nr < n and 0 <= nc < n:
                        danger[nr][nc] = 1
                        
    count = 0
    for r in danger:
        count += r.count(0)
        
    return count