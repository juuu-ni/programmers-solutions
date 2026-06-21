def solution(spell, dic):
    result = ''.join(sorted(spell))
    
    for i in dic:
        if ''.join(sorted(i)) == result:
            return 1
    return 2