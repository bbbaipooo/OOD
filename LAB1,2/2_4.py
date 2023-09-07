year=int(input('Enter year : '))

if year%2==0:
    years=int(int(year)/2)
    print('saimai is just 20, in base ',years,'!',sep='')
else:
    years=int(((int(year))-1)/2)
    print('saimai is just 21, in base ',years,'!',sep='')