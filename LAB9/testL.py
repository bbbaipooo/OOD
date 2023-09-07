# l=[5,6,7,8,9]
# print(l)
# print(l[:-1])
# print(l[:-2])
# print(l[::2])

def selectSort(l):return [l.pop(l.index(min(l))) for i in l.copy()]

l=list(map(int,input('Enter Input : ').split()))
print(selectSort(l))
    