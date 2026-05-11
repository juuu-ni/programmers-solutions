def solution(sizes):
    result = [[max(w,l),min(w,l)] for w,l in sizes]
    return max(w for w,l in result)*max(l for w,l in result)