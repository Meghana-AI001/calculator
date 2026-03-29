s="hello,python"
print(s[0:5])
print(s[:-3])
print(s[::-1])
print(s[::-2])
print(s[1:7:4])
for char in s:
    print(char)
s="H"+s[1:]
print(s)
s1="hello python"
s2=s1.replace("python","world")
print(s)
print(s2)
print(len(s1))
print(s1.upper())
print(s1.lower)
s3=" hello "
print(s3.strip())
print(s1+" "+s2)
print(s2*3)
name="abcd"
age=20
print(f"name:{name} and age is {age}")
s4="my name is {} and i am {} years old.".format("abcd",20)
print(s4)
print("python" in s1)
print("apple" in s1)
s5="my name is abcd"
a=s.split()
print(a)
print(list(s5))
s6="45"
print(int(s6))
s7="1010"
print(int(s7,2))
print(int(s7,16))
s8="abc"
try:
    num=int(s8)
    print(num)
except ValueError:
    print("invalid input:cannnot convert to integer")
s9="12334"
if s9.isdigit():
    num=int(s9)
    print(num)
else:
    print("the string is not numeric.")
