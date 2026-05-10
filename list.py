#find the mean of the list

l=[12,3,4,45,67,89,54,86,9,99]
sum=0

for i in l:
    sum= sum+i
print (sum/len(l))

# find the greasted element and print its index too

l= [12,34,54,65,78,54,76,87]
largest=l[0]
index = 0 
for i in range(len(l)):
    if l[i]>largest:
        largest = l[i]
        index= i
print(f"you largest no is {largest} at index{index}")



# find the 2nd largest number 

l= [12,34,54,65,78,54,76,87]

largest=[0]
second_lar = l[0]

for i in l:
    if i > largest:
        second_lar = largest
        largest=i
    elif i>second_lar:
        second_lar=i
print(second_lar, largest)


# check given list is sorted or not 

a=[12,13,14,15,16]

for i in range (len(a)-1):
    if a[i] < a[i+1]:
        continue
    else:
        print("your list is not sorted")
        break
else: 
    print("your list is shorted")
