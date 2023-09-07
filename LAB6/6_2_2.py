def len2(txt):
    if not txt : return 0
    if not txt[1:] : 
        print("{}*".format(txt[0]), end="")
        return 1
    print("{}*{}~".format(txt[0], txt[1]), end="")
    return 2+len2(txt[2:])
    
text=list(input('Enter Input : '))
print("\n",len2(text), sep='')