class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        poisoned = 0
        
        for i in range(len(timeSeries)-1):
            poisoned_period = timeSeries[i+1] - timeSeries[i]
        
            if poisoned_period >= duration:
                poisoned += duration
            else:
                poisoned += poisoned_period
            
        poisoned += duration
        
        return poisoned
        
            
        