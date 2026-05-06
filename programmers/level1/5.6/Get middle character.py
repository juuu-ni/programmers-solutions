def solution(s):
    lst_s = list(s)
    mid = len(s)//2
    if len(s)%2==0:
        return lst_s[mid-1]+lst_s[mid]
    else:
        return lst_s[mid]