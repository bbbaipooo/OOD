def bon(w):
    char=[]
    n=1
    for i in range(len(w)):
        for j in range(len(w)):
            if j==(len(w)):
                continue
            if w[i]==w[j+n]:
                return str(w[i])
                #w[i]=char
        n+=1
            
	

secretCode = input("Enter secret code : ")
print(bon(secretCode))