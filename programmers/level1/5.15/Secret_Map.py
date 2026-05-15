def solution(n, arr1, arr2):
    answer=[]
    for i in range(n):
        row1 =bin(arr1[i])[2:].zfill(n)
        row2 =bin(arr2[i])[2:].zfill(n)
        
        result=''
        for char1,char2 in zip(row1,row2):
            if char1=='1' or char2=='1':
                result+='#'
            else:
                result+=' '
        
        answer.append(result)
    return answer
