name= input("please enter your name")
age= int(input("please enter your age"))
if age >= 18:
    print(f"hello {name} you are eligible for voting")
else:
    print("you are not eligible for voting")
    print(f"hello{name} you are eligible after {18-age} year ")
