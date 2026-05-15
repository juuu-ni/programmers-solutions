def solution(s):
    arr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    tmp=''
    answer = ''
    for i in s:
        if i.isdigit():
            answer+=i
        else:
            tmp+=i
            if tmp in arr:
                answer+=str(arr.index(tmp))
                tmp=''
                
    return int(answer)