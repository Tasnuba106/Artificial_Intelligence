def fibonacci(n):
    if n <= 1:
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))
limit=int(input('Enter Limit: '))
for i in range(limit):
    print(fibonacci(i),end=' ')