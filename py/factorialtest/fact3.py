import math
# a=math.factorial(1000)
#print(a)
a=0
while 0==a:
    global n
    n=int(input("insert factorial n >>:"))
    def fact(n):
        return math.factorial(n)
    #fact(n)
    print(fact(n))
#for more information visit --> 
# https://stackoverflow.com/questions/40963848/recursive-factorial-calculator-recursionerror