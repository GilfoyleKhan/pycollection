n=int(input("enter fib number u want to end :>"))
def fib(n):
     a, b = 0, 1
     while a < n:
         print(a, end=' ')
         #a, b = b, a+b
         a=b
         b=a+b
     print("\n")
fib(n)

# a=b
#b=a+b