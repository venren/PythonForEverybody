
class LRUCache:
    
    def __init__(self, maxCapacity: int):
        self.map = {}
        self.usageMap = {}
        self.usageReverseMap = {}
        self.transactionCount = 0
        self.maxCapacity = maxCapacity

    def get(self, key: str):
        if key in self.map:
            self.transactionCount = self.transactionCount+1 
            self.usageMap[key] = self.transactionCount
            return self.map[key]
        
        return -1
        
    def put(self, key: str, val:int):
        self.transactionCount = self.transactionCount+1 
        if key in self.map:
            print("Key already present. overriding...\n")
        
        self.map[key] = val
        self.usageMap[key] = self.transactionCount
        self.cleanup()


    def cleanup(self):
        if len(self.map) <= self.maxCapacity:
            print("Nothing to clean up!!!")
            return

        lastUsedTransaction = self.transactionCount
        lastUsedKey = None

        for i, tran in self.usageMap.items():
            if tran < lastUsedTransaction:
                lastUsedTransaction = tran
                lastUsedKey = i

        if lastUsedKey is not None:
            del self.map[lastUsedKey]
            del self.usageMap[lastUsedKey]
            print(f"Removed last used key {lastUsedKey}") 


cache = LRUCache(2)
cache.put("1",1)     
cache.put("2",2)
print(cache.get("1"))
cache.put("3",3) #evicts key 2, cache is {1=1, 3=3}
print(cache.get("2"))    # returns -1 (not found)
cache.put("4", 4); # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
print(cache.get("1"));    # return -1 (not found)
print(cache.get("3"));    #return 3
print(cache.get("4"));    # return 4