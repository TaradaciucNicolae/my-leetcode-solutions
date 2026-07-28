# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

class LRUCache:


    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()
        

    def get(self, key: int) -> int:

        if key not in self.cache:
            return -1

        # Dacă cheia eixsta, tocmai o folosim
        # deci o mutam la final pentru a marca faptul ca este most recently used.
        self.cache.move_to_end(key)
        return self.cache[key]


        

    def put(self, key: int, value: int) -> None:

        if key not in self.cache:
            self.cache[key] = value # daca nu exista,  o adaugam
        
        else:
            self.cache[key] = value
            self.cache.move_to_end(key)

        # daca depasim capacitatea, eliminam least used
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
