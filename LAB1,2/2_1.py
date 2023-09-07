number = int(input(("Enter number to translate : ")))
staticNum = number
roman = []

while number > 0:
    if number//1000>=1:
        roman.append("M")
        number-=1000
    elif number//900>=1:
        roman.append("CM")
        number-=900
    elif number//500>=1:
        roman.append("D")
        number-=500
    elif number//400>=1:
        roman.append("CD")
        number-=400
    elif number/100>=1:
        roman.append("C")
        number-=100
    elif number//90>=1:
        roman.append("XC")
        number-=90
    elif number//50>=1:
        roman.append("L")
        number-=50
    elif number//40>=1:
        roman.append("XL")
        number-=40
    elif number//10>=1:
        roman.append("X")
        number-=10
    elif number//9>=1:
        roman.append("IX")
        number-=9
    elif number//5>=1:
        roman.append("V")
        number-=5
    elif number//4>=1:
        roman.append("IV")
        number-=4
    elif number//1>=1:
        roman.append("I")
        number-=1

for i in roman:
    print(i,end="")
print()
print(staticNum)