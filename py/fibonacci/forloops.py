def fibonacci(stop):
    global i
    a=0
    b=1
    print(a)
    for i in range(b,stop):

        a,b=b,a+b
        #c=a,b
        #print(f'{b} + {a}="\t"{b+a}')
        #print(b,"+",a,"=",' '*i,b+a)
        print(i,'~'*i,b+a)
    
num=fibonacci(int(input("insert a number :\t")))
print(num)


    