class TimeMap:

    def __init__(self):
        self.hset = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        lis = self.hset.get(key, [])
        lis.append((timestamp, value))
        self.hset[key] = lis
        

    def get(self, key: str, timestamp: int) -> str:
        lis = self.hset.get(key, [])
        if not lis:
            return ""
        l, r = 0, len(lis) - 1
        while l <= r:
            mid = l + (r - l)// 2
            if lis[mid][0] == timestamp:
                return lis[mid][1]
            if lis[mid][0] > timestamp:
                r = mid - 1
            else:
                l = mid + 1
        return lis[r][1] if r >=0 else ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
