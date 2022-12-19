salary=23.45
if salary<=10000:
    hra=salary*0.2
    da=salary*0.8
    g=salary+hra+da
elif salary<=10001 and salary>20000:
    hra=salary*0.25
    da=salary*0.9
    g=salary+hra+da
elif salary>=20001:
    hra=salary*0.3
    da=salary*0.95
    g=salary+hra+da
print("Salary=",g)

u=450.5
if u<=50:
    b=u*0.50
elif u<=150 and u>50:
    b=(50*0.50)+((u-50)*0.75)
elif u<=250 and u>150:
    b=(50*0.50)+(100*0.75)+((u-150)*1.20)
else:
    b=(50*0.50)+(100*0.75)+(100*1.20)+((u-250)*1.50)
print("Bill=",b)
s=b+p
p=(0.20*b)
print("Bill with surcharge=",s)