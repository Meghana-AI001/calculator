name=input("enter your name:")
age=int(input("enter your age:"))
city=input("enter city:")
hobby=input("enter hobby :")
print(f"name:{name},age:{age},city:{city},hobby:{hobby}")
birth_year=int(input("birth year:"))
present_year=int(input("present year:"))
present_age=present_year-birth_year
print(present_age)
if present_age<18:
    print("minor")
else:
    print("major")