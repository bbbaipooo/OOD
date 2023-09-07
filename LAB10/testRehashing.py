class hash:
    def __init__(self,table_size,max_collisions,threshold):
        self.table_size=table_size
        self.max_collisions=max_collisions
        self.threshold=threshold
        self.store=[None for i in range(self.table_size)]
        self.sequence=[]
        self.size=0
    def Overthres(self,val):
        if (self.size/self.table_size)*100>self.threshold:
            print("****** Data over threshold - Rehash !!! ******")
            self.rehas(val)
            return True
        return False
    def insert(self,value):
        pass
            