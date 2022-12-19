def strong_number(n):
    sum = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        sum =sum+factorial(digit)
        temp = temp // 10
    return n == sum
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
num = int(input("Enter a number: "))
if strong_number(num):
    print("{} [Strong Number]".format(num))
else:
    print("{} [Weak Number]".format(num))