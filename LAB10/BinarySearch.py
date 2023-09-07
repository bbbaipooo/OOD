# def bi_search(l, r, arr, x):  #binary searchก็แย่ละ!!!!!!!!!!!
#     if l>r:
#         return False
#     else:
#         if arr[r]==x:
#             return True
#         return bi_search(l,r-1,arr,x)   #******************
#     #return 0  *******************************


# def bi_search(l, r, arr, x):
#     mid = (r+l)//2#หาค่าตรงกลาง
#     if arr[mid]==x:return True#เจอค่า
#     elif l==r:return False#หมดลิสละไม่เจอค่า
#     elif x<arr[mid]:return bi_search(mid+1,r,arr,x)#ไปขวา
#     else:return bi_search(l,mid-1,arr,x)#ไปซ้าย 


# inp = input('Enter Input : ').split('/')
# arr, k = list(map(int, inp[0].split())), int(inp[1])
# print(bi_search(0, len(arr) - 1, sorted(arr), k))



def bi_search(lst, x):
    if len(lst)==0:
        return False
    mid=len(lst)//2
    if lst[mid]==x:
        return True
    elif lst[mid]<x:
        return bi_search(lst[mid+1:],x)
    elif lst[mid]>x:
        return bi_search(lst[:mid-1],x)


inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), int(inp[1])
print(bi_search(sorted(arr), k))
















# def binarysearch(List, x):
#     if len(List) == 0:
#         return False
#     mid = len(List)//2
#     if List[mid] == x:
#         return True
#     elif x > List[mid]:
#         return binarysearch(List[mid+1:], x)
#     elif x < List[mid]:
#         return binarysearch(List[:mid], x)


# IN, x = input("Enter Input : ").split('/')
# IN = sorted(list(map(int, IN.split())))
# print(binarysearch(IN, int(x)))




