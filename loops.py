x=int(input("Enter a number:"))
i=0
while i<x:
    i+=1
    if i%10==0:
        continue
    elif i>100:
        break
    print(i)