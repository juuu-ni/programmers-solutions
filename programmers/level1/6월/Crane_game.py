def solution(board, moves):
    stac = []
    answer = 0
    for move in moves:
        index = move -1
        for doll in board:
            if doll[index] !=0:
                stac.append(doll[index])
                doll[index] = 0
                
                if len(stac)>=2 and stac[-1]==stac[-2]:
                    answer+=2
                    stac = stac[0:-2]
                    
                break
            
    return answer