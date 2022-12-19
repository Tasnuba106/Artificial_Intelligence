num=int(inp('Enter a number: '))
n=num
i=2
while i<=n:
    if n%i==0:
        print(i)
        n=n/i
    else:
        i=i+1
if(n>1):
    print(n,end=' ')