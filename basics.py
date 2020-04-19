def greeting(value):
    name = input('Enter you name:')
    surname = input('Enter your surname')
    fullname = 'Hi %s %s' % (name,surname)
    return fullname
print(greeting('fullname'))

#date-time function
#import datetime
#mynow = datetime.datetime.now()
#print(mynow)

#list,dictionary & average of number inside
#grades=[5.6,7.2,6.3,9.1]
#stu_grades={"marry":9.3,"taps":9.1,"smruti":6.3}
#length=len(stu_grades)
#mysum=sum(stu_grades.values())
#avg=mysum/length
#print(avg)
#print(length)

#append method
#mon_temp1=(20,30,60)
#mon_temp2=[40,50,60]
#changetemp=mon_temp2.append(80)
#print(changetemp)

#function creation/declartion
#def mean(mylist):
    #the_mean = sum(mylist) / len(mylist)
    #return the_mean
#calling function
#print(mean([3,5,10,2]))
#print(type(mean),type(sum))

#function with if/else conditional
#def avg(value):
    #if type(value) == dict:
        #avg_mean= sum(value.values())/len(value)
    #else:
        #avg_mean= sum(value)/len(value)
    #return avg_mean
#grades={'kunu':30,'chana':40,'tapu':50}
#print (avg(grades))


#user input
#def weather(value):
    #if value >= 10:
        #return 'Warm'
    #else:
        #return 'Cold'
#usr_inp=float(input('enter the temp:')) #float() type converts the value to float and prevents from error 
#print('weather condition:',weather(usr_inp))
#print('the type of user input is:',type(usr_inp))

#string formatting with user input
#usr_inp = input('enter your name:')
#message = 'Hi %s' % usr_inp # %s(place holder) and % are special character used for string formatting in 3.6 or earlier version of python
#message = f'Hi {usr_inp}' #used in 3.6 or later version
#print(message)

'''string formatting with multiple user inputs
name = input('enter your name:')
surname = input('enter your surname:')
message = 'Hi %s %s' % (name,surname) # %s %s two place holders for two string inputs
message = f'Hi {name} {surname}' #multiple curly braces for multiple strings
print(message)

def greeting(value):
    name = input('Enter you name:')
    surname = input('Enter your surname')
    fullname = 'Hi %s %s' % (name,surname)
    return fullname
print(greeting('fullname'))'''

#for-loop
'''mon_temp = [3.2,6.8,7.2]
for temperature in mon_temp:
    print(round(temperature))
for letter in 'smruti':
    print(letter)

colors = [11, 34, 98, 43, 45, 54, 54]
for col in colors:
    if col > 50:
        print (col)

colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]
for col in colors:
    if type(col) == int:
        print (col)

colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]
for col in colors:
    if type(col) == int and col > 50:
        print (col)'''

'''grades={'kunu':30,'chana':40,'tapu':50}
for gr in grades.items():
    print(gr)'''


'''phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
for key,value in phone_numbers.items():
    print("{} has a number {}".format(key, value))

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
for ph in phone_numbers.items():
    print("{} has a number {}".format(ph[0], ph[1]))'''

'''phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
for ph in phone_numbers.values():
    print('{}'.format(ph.replace('+','00')))'''

'''def foo(lst):
    return [i for i in lst if not isinstance(i,str) ]
print(foo(['no data',99,22,'hi']))'''

'''def foo(lst):
    for i in lst:
        if i>0:
            print (i)
print (foo([1,2,3,-1,-4,-3,6]))'''

'''def foo(lst):
    return [i if not isinstance(i,str) else 0 for i in lst]
print (foo([33,22,'hi']))'''

'''def foo(*args):
    mean = sum(args)/len(args)
    return mean
print (foo(10,20,30,6))'''

'''file = open("fruits.txt")
print(file.read())
file.close()'''

'''with open("fruits.txt") as file:
    content = file.read()
print(content)'''

'''with open("veggies.txt","w") as file:
    file.write("tomato\nbroccoli\n")'''

'''with open("fruits.txt") as f:
    x = f.read()'''

'''import time
while True:
    with open("fruits.txt") as file:
        print(file.read())
        time.sleep(5)'''

import time
import os
if os.path.exists("xyz.txt"):
    with open("xyz.txt") as file:
        print(file.read())
else:
    print("file not found")
time.sleep(5)