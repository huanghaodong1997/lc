class UndergroundSystem:

    def __init__(self):
        self.average_mp = {}
        self.id_mp = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id in self.id_mp: return
        self.id_mp[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id not in self.id_mp: return 
        src_station, start = self.id_mp[id]
        key = (src_station, stationName) 
        if key not in self.average_mp:
            self.average_mp[key] = (0, 0)
        time, freq = self.average_mp[key]
        self.average_mp[key] = (time + (t - start), freq + 1)
        del self.id_mp[id]
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        time, freq = self.average_mp[(startStation, endStation)]
        return time / freq


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)