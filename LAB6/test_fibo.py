def fibo(n):
    if n == 1:
        return 0
    elif n == 2 or n == 3:
        return 1
    else:
        return fibo(n-2)+fibo(n-1)

num = int(input('Entter Input : '))
print(fibo(num))
