class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t < 0:
            return False

        n = len(nums)
        num_arr = []
        # create a array of tuple where first index hold the element
        # and 2nd Index hold its index
        for i in range(n):
            temp = (nums[i],i)
            num_arr.append(temp)

        # sort the array
        num_arr = sorted(num_arr)

        # loop through array from 0th position
        for i in range(n):
            # loop array from i+1 postion
            for j in range(i+1,n):
                # check if difference of two elements is less than t or not
                # if not, no need to check further as array is already sorted
                # so further element's different will also not meet this criteria
                if abs(num_arr[i][0] - num_arr[j][0]) <= t :
                    # if above condition met, check if both index's position defference is less than k
                    if abs(num_arr[i][1] - num_arr[j][1]) <= k:
                        # if yes, return True
                        return True
                else:
                    break
        return False