def solution(q, r, code):
    result=''
    for idx,char in enumerate(code):
        if idx%q==r:
            result+=char
    return result