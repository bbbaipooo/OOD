def findMax(list):
    if len(list)==1:
        return list[0]
    MAX=findMax(list[1:])
    return MAX if MAX>list[0] else list[0]
    



inp=input('Enter Input : ')
print(findMax(inp))