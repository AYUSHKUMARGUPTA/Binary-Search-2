# Time Complexity: O(log n), , n defines number of elements in the array
# Space Complexity: O(1)
class Solution:
    def findPeakElement(self, nums) -> int:
        n = len(nums)
        low = 0
        high = n - 1
        while low <= high:
            mid = low + (high-low)//2
            if ((mid==0 or nums[mid]>nums[mid-1]) and (mid==n-1 or nums[mid]>nums[mid+1])):
                return mid
            elif mid>0 and nums[mid-1]>nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return 0