year= int(input("enter year"))
if year % 100 ==0 and year % 400 ==0:
    print("its a leap year")
elif year%100 !=0 and year%4 ==0:
    print("its a leap year")
else:
    print("not a leap year")