def isPalindrome(t):
    charAtoZ='abcdefghijklmnopqrstuvwxyz'
    if t[0] not in charAtoZ:
        if len(t)==1:
            return 'Palin'
        return isPalindrome(t[1:])
    if t[-1] not in charAtoZ:
        return isPalindrome(t[:-1])
    
    if len(t)==0 or len(t)==1:
        return 'Palin'
    elif len(t)==2 and t[0].lower()==t[-1].lower():
        return 'Palin'
    elif t[0].lower()==t[-1].lower():
        return isPalindrome(t[1:-1])
    else:
        return 'not palin'


inp=input('Enter Input : ')
print(isPalindrome(inp))