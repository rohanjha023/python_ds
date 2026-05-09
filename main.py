t= int (input("enter your temperature"))
if t<0:
    print("freezing cold")
elif (t>=0 and t<10):
     print("very cold")
elif (t>=10 and t<20):
     print("cold")
elif (t>=20 and t<30):
     print("pleasant")
elif (t>=30 and t<40):
     print("hot")
else:
     print("very hot")