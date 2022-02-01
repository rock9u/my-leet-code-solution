class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        absDeg = abs(self.getHourDeg(hour,minutes)-self.getMinDeg(minutes))
        return absDeg if absDeg <= 180 else 360 - absDeg
        
    
    def getHourDeg(self,hour,minutes):
        return 30 * (hour%12) + 0.5 *minutes 
        
    def getMinDeg(self,minutes):
        return 6*minutes