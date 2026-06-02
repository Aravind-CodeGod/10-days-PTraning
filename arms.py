n=int(input())
n1=n
c=n
a=0
c=0
while(n1>0):
    r=n1%10
    c+=1
    n1=n1//10
while(n>0):
    r=n%10
    a=a+r**c
    n=n//10
if(c==a):
    print("Arms")
else:
    print("Not arms")``