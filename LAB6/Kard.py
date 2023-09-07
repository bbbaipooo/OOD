def GCD(x, y):
    if y == 0:
        return x
    return GCD(abs(y), abs(x % y))


x, y = map(int, input("Enter Input : ").split())
if x == 0 and y == 0:
    print("Error! must be not all zero.")
elif x > y:
    print(f"The gcd of {x} and {y} is : {GCD(x,y)}")
else:
    print(f"The gcd of {y} and {x} is : {GCD(y,x)}")
