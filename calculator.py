try:
    a=float(input("Enter 1st number:"))
    op=input("Enter operator any one '+,-,*,/,**,%,//:")
    b=float(input("Enter 2nd number:"))
    if op=="/" and b==0:
        print("Error: division by zero")
    else:
        result={
            "+":a+b,
            "-":a-b,
            "*":a*b,
            "/":a/b,
            "%":a%b,
            "**":a**b,
            "//":a//b
        }.get(op,"Invalid operator")
        if isinstance(result,str):
            print(result)
        else:
            print(f"Result :{result:.4f}")
except ValueError:
    print("Invalid input.enter numbers only")
        