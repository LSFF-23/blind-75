class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = 0
        last = len(nums) - 1
        mid = (first + last) // 2
        
        while first < last:
            if nums[first] <= nums[mid] and nums[mid] <= nums[last]:
                return nums[first]
            if nums[first] < nums[mid] and nums[mid] > nums[last]:
                first = mid + 1
            elif nums[first] > nums[mid] and nums[mid] < nums[last]:
                last = mid
            else:
                first += 1
            mid = (first + last) // 2
        
        return nums[mid]     

s = Solution()
assert s.findMin([1, 2, 3]) == 1, "#1"
assert s.findMin([11,13,15,17]) == 11, "#2"
assert s.findMin([2, 3, 4, 5, 6, 7, 1]) == 1, "#3"
assert s.findMin([3,4,5,1,2]) == 1, "#4"
assert s.findMin([4,5,6,7,0,1,2]) == 0, "#5"
assert s.findMin([0]) == 0, "#6"
assert s.findMin([2,1]) == 1, "#7"
assert s.findMin([3,1,2]) == 1, "#8"
assert s.findMin([5,1,2,3,4]) == 1, "#9"