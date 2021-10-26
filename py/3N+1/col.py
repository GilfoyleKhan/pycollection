#collazt sequence
def collatz(num,char):
    if num==1:
        #print(num)
        return num
    elif num%2==0:
        num=num/2
        #print(num)
        print(f"{int(num)*char,int(num)}")
        return collatz(num,char)
    else:
        num=num*3+1
        #print(num)
        print(f"{int(num)*char,int(num)}")
        return collatz(num,char)
while True:
    number=int(input("Number? \t:"))
    char=str(input("String? \t:"))
    collatz(number,char)
