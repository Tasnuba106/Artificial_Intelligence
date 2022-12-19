s = inp("Enter the following string: ")
length = len(s)
st = list(s)
for i in range (0,length):
    if(st[i] == '!' or st[i] == '%'):
        st[i] = '*'

    elif(st[i] == '`'):
        st[i] = '*'

for i in range(0,length):
    print(st[i],end="")

print()