def solution(score):
    avg = [(a + b) / 2 for a, b in score]

    result = []
    for x in avg:
        rank = 1
        for y in avg:
            if y > x:
                rank += 1
        result.append(rank)

    return result