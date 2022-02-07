class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left=0
        counter = 1
        for i in range(1, len(nums)):
            if nums[left] == nums[i]:
                counter += 1
            else:
                counter = 1
      
            if counter <= 2:
                left += 1
                nums[left] = nums[i]
        return left + 1