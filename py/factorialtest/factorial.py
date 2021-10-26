#for more information visit --> 
#https://stackoverflow.com/questions/40963848/recursive-factorial-calculator-recursionerror
#import sys
#sys.setrecursionlimit(2000)

a=0
while True:
    n=int(input("insert factorial n >>:"))#5
    def fact(n):
        if n==1:
            return 1
        else:
            return n*fact(n - 1)
    print(n*fact(n - 1))
#just copy below to code faster
# from math import factorial
# print(factorial(5))
#
#



    
            