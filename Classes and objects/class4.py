class internship:
    i=int(input("enter the no. of students eligible to take internship : "))
    n=20
    if i < n:
        print("Students should do intern",i)
    else:
        print("Not Eligible")
k=internship()
print("The number you entered is : ",k.i)