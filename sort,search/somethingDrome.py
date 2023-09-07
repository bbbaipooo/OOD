def Metadrome(lst,i,n):
    if i==n:return True
    else:
        if lst[i]>=lst[i+1]:return False
        return Metadrome(lst,i+1,n)
def Plaindrome(lst,i,n):
    if i==n:return True
    else:
        if lst[i]>lst[i+1]:return False
        return Plaindrome(lst,i+1,n)
def Katadrome(lst,i,n):
    if i==n:return True
    else:
        if lst[i]<=lst[i+1]:return False
        return Katadrome(lst,i+1,n)
def Nialpdrome(lst,i,n):
    if i==n:return True
    else:
        if lst[i]<lst[i+1]:return False
        return Nialpdrome(lst,i+1,n)
def Repdrome(lst,i,n):
    if i==n:return True
    else:
        if lst[i]!=lst[i+1]:return False
        return Repdrome(lst,i+1,n)
    

inp=list(map(int,input('Enter Input : ').split()))
if Repdrome(inp,0,len(inp)-1):
    print('Repdrome')
elif Metadrome(inp,0,len(inp)-1):
    print('Metadrome')
elif Plaindrome(inp,0,len(inp)-1):
    print('Plaindrome')
elif Katadrome(inp,0,len(inp)-1):
    print('Katadrome')
elif Nialpdrome(inp,0,len(inp)-1):
    print('Nialpdrome')
else:
    print('Nondrome')
