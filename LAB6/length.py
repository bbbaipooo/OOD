def len2(text):
    if not text:
        return 0
    if not text[1:]:
        print(f'{text[0]}*',end='')
        return 1
    print(f'{text[0]}*{text[1]}~',end='')
    return 2+len2(text[2:])
    
    
print("\n",len2(input('Enter Input : ')), sep='')