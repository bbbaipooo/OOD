def isPalindrome(t):
    if t[0] not in cAtoZ:
        return isPalindrome(t[1:])
    if t[-1] not in cAtoZ:
        return isPalindrome(t[:-1])
        
    if len(t)<=1: 
        return ' is Palindrome'
    elif t[0]==t[-1]:
        re=isPalindrome(t[1:-1])   #******************start,-end-,step
    else:
        return ' is not Palindrome'
        
cAtoZ='abcdefghijklmnopqrstuvwxyz'
inp=input('Enter input : ')
m=inp.lower()

print('\'',inp,'\'',isPalindrome(m),sep='')