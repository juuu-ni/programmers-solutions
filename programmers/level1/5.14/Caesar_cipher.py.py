def solution(s, n):
    answer = ''
    for i in s:
        if i == ' ':
            answer+=i
        else:
            k = chr(ord(i)+n)
            if k.isupper() != i.isupper() or not k.isalpha():
                k= chr(ord(i)+n-26)
            answer +=k
            
    return answer