import random
x1=int(input())
x2=int(input())
a=random.randint(x1,x2)
n=0
while True:
    b=int(input())
    if b>a:
        print('太高')
        n=n+1
    elif b<a:
        print('太低')
        n=n+1
    else :
        n=n+1
        print('正確')
        print('總共猜了',n,'次')
        break
    
