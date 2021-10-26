evenodd=int(input(""" 
1.even or odd
2.list all even&odd numbers """))
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
    for i in range(start,end,skip):
        print(f"{i}")
else:
    print("error")