def pallindrome(st):
    rev= ""
    for i in range (len(st)-1,-1,-1):
        rev=rev+st[i]
    if rev== st:
        print("pallindrome")
    else:
        print("not a pallindrome")
pallindrome("NAMAN")
pallindrome("CURSER")