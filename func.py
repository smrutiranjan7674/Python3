'''def calc(a,b):
    add=a+b
    prod=a*b
    sub=a-b
    return add,prod,sub
check=calc(10,20)
print(check)'''

#global & local vars
'''x=123
def display():
    x=234
    print (x)
    print(globals()['x']) #to access the global var inside a func
print(x)
d=display #assigning variable to a func
d()'''

#passing function as a parameter
'''def greeting(name):
    return "Hello "+name
def check():
    return "smruti"
print(greeting(check()))'''

#nested function
def greeting(name):
    def check():
        return "Hi"
    fullname= check() +name
    return fullname
print(greeting("smruti"))

