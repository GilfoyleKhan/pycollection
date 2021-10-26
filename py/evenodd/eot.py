print(""" 
loop=1
while loop==1:
    evenodd=int(input(" 
    1even or odd
    2.list all even&odd numbers "))
    if evenodd==1:
        eo=int(input("enter>"))
        if eo%2==0:
            print(f'{eo} is even')
        else:
            print(f"{eo} is odd")
    elif evenodd==2:
        print("")
        skip=int(input("enter skipping digit:>>:"))
        end=int(input("enter ending digit:>>:"))
        start=int(input("enter starting digit:>>:"))
        all=int(input("1.list all odd numbers\n2.list all even numbers"))
        for i in range(start,end,skip):
            if all==2:#even
                if i%2==0:
                    print(f'{i}')#even
                else:
                    break
            else:
                if i%2!=0:
                    print(f'{i}')#even
                else:
                    break

    else:
        print("error")
""")