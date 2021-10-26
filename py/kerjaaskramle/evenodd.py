a=0
while a==0:
    global num
    #num=int(input("ENTER NUMBER to justify odd or even >--> : "))
    num=int(input("ENTER NUMBER to justify odd or even >--> : "))
    def evenodd(num):
        if num%2==0:
            print("\t",num,"is even number\t")
        else:
            print("\t",num,"is odd number\t")
    evenodd(num)

#for odd in range(1,15,2):
 #   print(odd)
        