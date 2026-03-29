password=input("enter password")
isalnum=True
if len(password)>=8 and isalnum and any(c.isupper() for c in password):
    print("strong password")
else:
    print("weak passoword, please be it atleast 1 capitl ,1 special character and 1 numerical value")