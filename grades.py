
x=int(input("Enter math marks:"))
y=int(input("Enter physics marks:"))
z=int(input("Enter chemistry marks:"))
avg=(x+y+z)/3
if (x or y or z) <= 34:
    print("fail")
elif avg <= 59:
    print("grade is c")
elif avg <= 69:
    print("grade is B")
elif avg >= 70:
    print("grade is a")

