'''def length(txt):
    count=0
    countc=0
    if countc%2==0:
        count+=1
        countc+=1
        t+=txt.pop(0)+'*'
    elif countc%2==1:
        count+=1
        countc+=1
        t+=txt.pop(0)+'~'
    elif txt[0]==' ':
        countc==0
        t+=' '
    elif txt==None:
        text=t
        return text
    return length(txt)'''

def len2(txt):
    if not txt : return 0 #not txt =txtไม่เป็นstring
    if not txt[1:]: #txt[1:]
        print("{}*".format(txt[0]), end="")
        return 1
    print("{}*{}~".format(txt[0], txt[1]), end="")
    return 2+len2(txt[2:])
    
text=list(input('Enter input : '))
print("\n",len2(text), sep='')
#t=''
#print(length(text))