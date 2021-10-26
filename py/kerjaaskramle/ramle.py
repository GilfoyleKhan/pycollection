#global x,y
def besarkecil(x,y):
    if y>x:
        return x,y
    else:
       return y,x
x=int(input("enter >>"))
y=int(input("enter >>"))
print(f'>>{besarkecil(x,y)}<<')