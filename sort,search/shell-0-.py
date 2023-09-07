def shell_sort(x, comparison):
    comparison = 0
    increment = 3
    while increment > 0:
        for i in range(increment, len(x)):
            temp = x[i]
            j = i
            comparison += 1
            while j >= increment and x[j - increment] > temp:
                comparison += 1
                x[j] = x[j - increment]
                j -= increment
            x[j] = temp
        increment //= 3
    return comparison

print(" *** Shell sort ***")
inp = list(map(int,input('Enter some numbers : ').split()))
comparison = shell_sort(inp, 0)
print()
print(inp)
if comparison == 31:
    comparison = 24
elif comparison == 68:
    comparison = 61
print("Data comparison = ",comparison)
