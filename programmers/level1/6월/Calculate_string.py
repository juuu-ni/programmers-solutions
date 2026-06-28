def solution(my_string):
    new = my_string.split()
    
    num = int(new[0])
    
    for i in range(1,len(new),2):
        opr = new[i]
        next = int(new[i+1])
        
        if opr == "+":
            num += next
        elif opr == "-":
            num -= next
            
    return num
        