#print table of 5
for i in range(5,51,5):
     print(i)

# table of n no

n=int(input("please enter the no you want to print table"))
for i in range (n,n*10+1,n):
     print(i)


#for loop in string
a= "python is very popular language"
for i in range(len(a)):
     print(a[i])

#accept an integer and print n times hello world

n= int(input("please tell your number"))
for i in range(n):
    print("hello world")

#print natural number up to n 

n= int(input("enter your natural number"))
for i in range(1,n+1):
    print(i)


#reverse for loop print n to 1 
n= int(input("enter your number"))
for i in range(n,0,-1):
    print(i)
 



#sum up to n terms
n= int(input("enter your number"))
sum=0
for i in range(1,n+1):
    sum=sum+i
print(sum)


# print factorial of a number

n= int(input("enter your number for factorial  "))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)


# print the sum of all even and odd no in a range seperately
n= int(input("enter your number"))
even= 0
odd=0
for i in range(1,n+1):
    if i%2== 0:
        even = even+i
    else:
        odd=odd+i
print(f"sum of even is {even} and the sum of odd is {odd} ")



#print all the factor of a number
n= int(input("enter your number"))
for i in range(1,n+1):
    if n%i== 0:
        print(i)




#check whether a number is perfect no or not 
#6- factor add factor add factor 1+2+3 =6 = perfect no 
n= int(input("enter your number"))
sum = 0
for i in range(1,n):
    if n%i== 0:
        sum= sum+i
if sum==n:
    print("no is perfect")
else: 
    print()

    

# check wether the number is prime or not

n= int(input("enter your number"))
count=0
for i in range(1,n+1):
    if n%i== 0:
        count= count+1
if count==2:
    print ("no is prime ")
else:
    print("not a prime no")

# reverse string without using build functions 
# check the # is palindrome or not 
#count all letters digits and special symbols from a given #string

a= "NAMAN"
b = ""
for i in range(len(a)-1,-1,-1):
    print(a[i])

if b==a:
    print("your string is pallindrome")

else:
    print("its not a pallindrome")