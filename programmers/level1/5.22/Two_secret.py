def solution(s, skip, index):
    alpha = [i for i in 'abcdefghijklmnopqrstuvwxyz' if i not in skip]
    result = ''
    
    for a in s:
        answer = alpha.index(a)
        result +=alpha[(answer + index)%len(alpha)]
            
    return result

