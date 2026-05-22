def solution(keymap, targets):
    min_press = {}
    for key in keymap:
        for i, c in enumerate(key):
            if c not in min_press or min_press[c] > i + 1:
                min_press[c] = i + 1
    
    result = []
    for target in targets:
        total = 0
        for c in target:
            if c not in min_press:
                total = -1
                break
            total += min_press[c]
        result.append(total)
    
    return result