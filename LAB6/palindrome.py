'''def isPalindrome(t):
    if t[0].lower() not in cAtoZ:
        return isPalindrome(t[1:])
    if t[-1].lower() not in cAtoZ:
        return isPalindrome(t[:-1])
        
    if len(t)<=1: 
        return ' is Palindrome'
    elif t[0].lower()==t[-1].lower():
        re=isPalindrome(t[1:-1])   #******************start,-end-,step
    else:
        return ' is not Palindrome'
        
cAtoZ='abcdefghijklmnopqrstuvwxyz'
inp=input('Enter input : ')

print('\'',inp,'\'',isPalindrome(inp),sep='')'''

def isPalindrome(t):
    cAtoZ='abcdefghijklmnopqrstuvwxyz'
    if t[0].lower() not in cAtoZ:
        if len(t)==1:
            return True
        return isPalindrome(t[1:])
    if t[-1].lower() not in cAtoZ:
        return isPalindrome(t[:-1])      
    if len(t)<=1: 
        return True
    elif len(t)==2 and t[0].lower()==t[-1].lower():
        return True
    elif t[0].lower()==t[-1].lower():
        return isPalindrome(t[1:-1])   #******************start,-end-,step
        

inp=input('Enter input : ')

if isPalindrome(inp):
    print('Palin ')
else:
    print('Not Palin')










