def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    if n2>n1:
        return n2-n1
    else:
        print(n1-n2)
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2
print("chhose options"
      "1.add"
      "2.sub"
      "3.mul"
      "4.div")
sel=int(input("select opration from 1 to 4"))
n1=int(input("enter 1st number"))
n2=int(input("enter 2nd number"))
if sel==1:
    print(n1,"+",n2,"=",add(n1,n2))
elif sel==2:
    print(n1,"-",n2,"=",sub(n1,n2))
elif sel==3:
    print(n1,"*",n2,"=",mul(n1,n2))
elif sel==4:
    print(n1,"/",n2,"=",div(n1,n2))
else:
    print("invald operation")
    