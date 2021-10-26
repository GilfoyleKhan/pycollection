a=0
while True:
    global n
    n=int(input("enter >>?"))
    def th(n):
        if n==1:
            return 1#1 is also an odd number,to avoid wasting time,
                   #we just return one because there will be an infinite recursion.
                   #That is the main of the problem in 3N+1
                   #calculation explanation :
                   #    (1) *3+1 = 4
                   #    (4)/2 = 2
                   #    (2)/2 = 1
                   #    (1) *3+1 = 4
                   # and this will go on without stopping and create and infinite recursion
                   # or maybe it will create recursion error.That is why there return 1,
                   # so there will be no recurssion error as an output
        if n%2==0:#even
            print(n,f'/2')#presenting the outcome of 'n' and what makes the current value of n
            n=n/2#to set new value for the outcome of n divided by 2
            return th(n)#/2 
        else:#odd
            print(n,f'*3+1')#presenting the outcome of 'n' and what makes the current value of n
            n=n*3+1#to set new value for the outcome of n *3+1
            return th(n)#*3+1  
    
    th(n)
    print("1.0  -->end the loop")
    print(f'Number that you entered-->>{n}<<--')

    