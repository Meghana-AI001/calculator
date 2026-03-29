# Safe division using the guardian pattern
x = 6
y = 0
if y != 0 and (x / y) > 2:
    print("Division is safe and the result is > 2")
# This code will not crash because the division (x/y) is skipped when y is 0.
       