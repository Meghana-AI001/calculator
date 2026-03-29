 
def greet():
    msg="hello"
    print(msg)
greet()
msg1="python"
def display():
    print(msg1)
display()
print(msg1)
s = "Python is great!"

# def fun():
#     global s
#     s += "pythonn"
#     print(s)
#     s = "Look for  Python Section"
#     print(s)

# fun()
# print(s)
def a():
    print("helllo")
var=a
var()

x = 123

def display():
    x = 98   
    print(x)  
    print(globals()['x'])

print(x) 

a = display  
a()
a()

def fun(num):
    if num%2==0:
        print("even")
    else:
        print("odd")
a=fun
a(int(input("enter a number:")))

def fun(num):
    return num*40
a=fun
print(a(int(input("enter a number:"))))

# a="python"
# res=f"this is {a} programming"
# print(res)

a="hello"
b="world"
res="{} {}".format(a,b)
print(res)

c="python"
d="programmming"
result=c+" "+d
print(result)