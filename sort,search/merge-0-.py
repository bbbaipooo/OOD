comparison = 0
def merge(ls):
    global comparison
    if len(ls) > 1:
        mid = len(ls)//2
        left = ls[:mid]
        right = ls[mid:]
        merge(left)
        merge(right)
        x, y, z = 0, 0, 0
        while x < len(left) and y < len(right):
            if left[x] < right[y]:
                ls[z] = left[x]
                x += 1
            else:
                ls[z] = right[y]
                y += 1
            z += 1
            comparison += 1
        while x < len(left):
            ls[z] = left[x]
            x += 1
            z += 1
        while y < len(right):
            ls[z] = right[y]
            y += 1
            z += 1

def printAns(inp):
    for e in range(len(inp)):
        print(inp[e], end=" ")

print(' *** Merge sort ***')
inp = [int(e) for e in input('Enter some numbers : ').split(' ')]
merge(inp)
print("\nSorted -> ", end='')
printAns(inp)
print('\nData comparison = ', comparison)

