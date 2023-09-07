class hash:
    def __init__(self, table_size, max_collosions,threshold):
        self.table_size = table_size
        self.max_collosions =max_collosions
        self.threshold =threshold
        self.store = [None for _ in range(self.table_size)]
        self.sequence=[]
        self.size = 0
    def  Overthres(self, val):
        if(self.size/self.table_size) * 100 > self.threshold:
            print("****** Data over threshold - Rehash !!! ******")
            self.rehash(val)
            return True
        return False
    def insert(self,value):
        self.size+=1
        if self.Overthres(value):
            return
        
        hashed_v = value%self.table_size

        first_hash_v = hashed_v

        collision_c = 0
        while self.store[hashed_v] is not None:
            collision_c +=1
            print(f"collision number {collision_c} at {hashed_v}")

            if collision_c >= self.max_collosions:
                print("****** Max collision - Rehash !!! ******")
                self.rehash(value)
                return
            
            n= collision_c
            hashed_v = (first_hash_v +n *n)%self.table_size
        self.store[hashed_v]=value
        self.sequence.append(value)
    def is_Prime(self,x):
        return all(x % i for i in range(2,x))
    def next_Prime(self,x):
        return min([a for a in range(x+1 , 2*x) if self.is_Prime(a)])
    def rehash(self,val):
        self.table_size =self.next_Prime(self.table_size*2)
        self.size = 0

        self.store = [None for _ in range(self.table_size)]

        arr =self.sequence.copy()
        self.sequence.clear()
        for ele in arr:
            if ele is not None:
                self.insert(ele)
        self.insert(val)

    def print_table(self):
        for i,ele in enumerate(self.store):
            print(f"#{i+1}\t{ele}")

print(" ***** Rehashing *****")
arr, arr1 = input("Enter Input : ").split("/")
table_size, max_collisions , threshold = list(map(int,arr.split(" ")))
arr =arr1.split(' ')


hash_table = hash(table_size, max_collisions,threshold)
print("Initial Table :")
hash_table.print_table()
print("----------------------------------------")
for ele in arr:
    print(f"Add : {ele}")
    hash_table.insert(int(ele))
    hash_table.print_table()
    print("----------------------------------------")