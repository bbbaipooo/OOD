def checkMeta(val):
    b=val[:-1]
    for i in range(len(b)):
        if b[i]>=val[i+1]:
            return False
    return True

def checkPlain(val):
    b=val[:-1]
    for i in range(len(b)):
        if b[i]>val[i+1]:
            return False
    return True

def checkKata(val):
    b=val[:-1]
    for i in range(len(b)):
        if b[i]<=val[i+1]:
            return False
    return True
    
def checkNial(val):
    b=val[:-1]
    for i in range(len(b)):
        if b[i]<val[i+1]:
            return False
    return True
    
def checkRep(val):
    b=val[:-1]
    for i in range(len(b)):
        if b[i]!=val[i+1]:
            return False
    return True

    
inp=input('Enter Input : ')
if checkRep(inp):print("Repdrome")
elif checkMeta(inp):print("Metadrome")
elif checkPlain(inp):print("Plaindrome")
elif checkKata(inp):print("Katadrome")
elif checkNial(inp):print("Nialpdrome")
else: print("Nondrome")