class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i=0
        j=0
        index=0
        c=None
        p=None
        while i<len(nums1) and j<len(nums2) and index<=(len(nums1)+len(nums2))//2:
            p=c
            if nums1[i] < nums2[j]:
                c = nums1[i] 
                i += 1 
                index += 1  
            else:  
                c = nums2[j]
                j += 1  
                index += 1
                
        while i<len(nums1) and index<=((len(nums1)+len(nums2))//2):   
            p=c
            c=nums1[i]
            i+=1
            index+=1
        
        while j<len(nums2) and index<=((len(nums1)+len(nums2))//2):
            p=c
            c=nums2[j]
            j+=1
            index+=1
        
        if (len(nums1)+len(nums2))%2!=0:
            return c
        else:
            return (c+p)/2
            
        
        
        