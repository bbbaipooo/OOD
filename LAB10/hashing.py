class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)


class hash:
    def __init__(self, tableSize, maxColli):
        self.tableSize = tableSize
        self.maxColli = maxColli
        self.size = 0
        self.table = [None for i in range(tableSize)] # ex.tSize=3  [None,None,None]

    def insert(self, data):
        data = data.split()

        sum = 0
        for i in data[0]:
            sum += ord(i)
        indexTable = sum % self.tableSize
        hashX = indexTable  # เพื่อคิดcolli
        colli = 0
        # if self.table[indexTable] == None:
        #     self.table[indexTable] = Data(data[0], data[1])
        #     self.size += 1
            
        while self.table[indexTable] is not None:
            colli+=1
            print(f'collision number {colli} at {indexTable}')
            if colli==self.maxColli:
                print('Max of collisionChain')
                return
            indexTable=(hashX+(colli*colli))%self.tableSize
            
        self.table[indexTable] = Data(data[0], data[1])
        self.size += 1
        # for i in self.table:
        #     print(i,'sos')
        
        #print(self.table)    #hateeeeeeeeeeeeeeeeeeee
    
    def isFull(self):
        if self.size==self.tableSize:
            return True
        return False
            
    def printTable(self):
        for i,j in enumerate(self.table):  #enumrateออกindexมาด้วย
            print(f'#{i+1}	{j}')
            
#         คำสั่ง enumerate ใน Python
# enumerate เป็นคำสั่งสำหรับแจกแจงค่า index และข้อมูลใน index ในรูปแบบทูเพิล (Tuple)
# ดังนี้ (Index,Value) โดยต้องใช้กับข้อมูลชนิด list
# เช่น
# ผลลัพธ์
# Index : 0 Value : 3
# Index : 1 Value : 6
# Index : 2 Value : 8
# Index : 3 Value : 2
        
        
    
        # count=1
        # for i in self.table:
        #     print(f'#{count}      {i}')
        #     count+=1
        
           
# Enter Input : 3 2/1+1 I,OnE Love,abcde I,#$ew2 KMITL,kk KMITL,z Love


print(' ***** Fun with hashing *****')
inp = input('Enter Input : ').split('/')
table, maxCollision = map(int, inp[0].split())
data = inp[1].split(',')
h=hash(table,maxCollision)
for i in data:
    if h.isFull()==False:
        h.insert(i)
        h.printTable()
        print('---------------------------')
    else:
        print('This table is full !!!!!!')
        break
    

        
        

