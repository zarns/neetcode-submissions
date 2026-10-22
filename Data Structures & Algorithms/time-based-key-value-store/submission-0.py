class TimeMap:

    def __init__(self):
        self.names = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.names:
            self.names[key].append((timestamp, value))
        else:
            self.names[key] = [(timestamp,value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.names:
            return ""
        timestamps = self.names[key]
        if timestamp < timestamps[0][0]:
            return ""
        l = 0
        r = len(timestamps)-1
        ans=""
        while l <= r:
            mid = (l+r)//2
            if timestamp < timestamps[mid][0]:
                r = mid - 1
            else:
                ans = timestamps[mid][1]
                l = mid+1
        return ans
