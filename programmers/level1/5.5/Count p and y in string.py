def solution(s):
    sLower = s.lower()
    if sLower.count("p") == sLower.count("y"):
        return True
    elif sLower.count("p") + sLower.count("y") == 0:
        return True
    else:
        return False
