from math import *

def t(n):
    n=n/2
    if n<2:
        print(n)
        return n
    else:
        n=n/2
        print(n)
        return t(n)
j=20
for i in range(10):
    print("___",i,"___")
    t(factorial(i))

#for i in range(5,100):
 #   print(eo(factorial(i)),f'=',i,'!')
  #  print(f'{eo(factorial(i))}\t={i}!={factorial(i)}')
