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
    
def checkRep(val):##ต้องเอาขึ้นก่อน ลองterminalดู
    b=val[:-1]
    for i in range(len(b)):
        if b[i]!=val[i+1]:
            return False
    return True
    
    

inp=input('Enter Input : ')
print(checkMeta(inp))
print(checkPlain(inp))
print(checkKata(inp))
print(checkNial(inp))
print(checkRep(inp))