def solution(babbling):
    possible = ['aya', 'ye', 'woo', 'ma']
    result = 0
    for word in babbling:
        for p in possible:
            if p*2 not in word: 
                word = word.replace(p, ' ')
        if word.strip() == '':
            result += 1
    return result