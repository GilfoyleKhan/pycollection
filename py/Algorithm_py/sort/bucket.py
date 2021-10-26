etc=[47,'name',23,'string',56,'v=chr',87]
index=0
while index<len(etc):
    if (type(etc[index])==int)==True:
        inti= etc[index]
        print(inti,end=' ')
    else:
        stri= etc[index]
        print(stri,end=' ')
    index+=1
#output :
#47 name 23 string 56 v=chr 87
