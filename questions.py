1Q) https://codeforces.com/problemset/problem/4/A

n=int(input())
if(n%2!=0 or n==2):
    print("No")
else:
    print(Yes")


2Q)https://codeforces.com/problemset/problem/791/A
a,b=map(int,input().split())
c=0
while(a<=b):
    a*=3
    b*=2
    c+=1
print(c)