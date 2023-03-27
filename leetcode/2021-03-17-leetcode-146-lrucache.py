import collections


class LRUCache:
    
    def __init__(self, capacity: int):
        self.cache = collections.OrderedDict()
        self.capacity = capacity
    
    def get(self, key: int) -> int:
        if key in self.cache:
            # 맨 오른쪽으로 이동 (조회되었으므로 오른쪽 이동)
            self.cache.move_to_end(key, last=True)
            return self.cache[key]
        else:
            return -1
    
    def put(self, key: int, value: int) -> None:
        # key값 존재시 update
        if key in self.cache:
            # 맨 오른쪽 이동
            self.cache.move_to_end(key, last=True)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            # FIFO
            self.cache.popitem(last=False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


if __name__ == '__main__':
    input_method = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    input_value = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    
    lru_cache = LRUCache(input_value[0][0])
    ans=[]
    ans.append('null')
    for idx in zip(input_method, input_value):
        print(idx[0], idx[1])
        if idx[0] == 'put':
            lru_cache.put(idx[1][0], idx[1][1])
            ans.append('null')
        elif idx[0] == 'get':
            ans.append(lru_cache.get(idx[1][0]))
        print("Result Cache : ",lru_cache.cache)
        print("***********************")
        
    print(ans)
           
