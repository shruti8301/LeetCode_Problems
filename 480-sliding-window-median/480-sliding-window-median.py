class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        i=0
        j=k
        arr=[]
        def median_for_even(array):
            return (array[len(array)//2-1]+array[len(array)//2])/2
                
        def median_for_odd(array):
            return array[len(array)//2]
        def sortArray(array):
            return sorted(array)
        while j<=len(nums):
            first_sorted=sortArray(nums[i:j])
            if len(first_sorted)%2==0:
                median=median_for_even(first_sorted)
            if len(first_sorted)%2!=0:
                median=median_for_odd(first_sorted)
            
            j+=1
            i+=1
            arr.append(median)
        return arr