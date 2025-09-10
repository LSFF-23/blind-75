class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        first = 0
        last = len(nums) - 1
        rIndex = 0 if nums[first] <= nums[last] else -1
        while rIndex < 0 and first <= last:
            mid = first + (last - first) // 2
            before = nums[mid - 1] if mid - 1 >= 0 else nums[mid]
            after = nums[mid + 1] if mid + 1 < len(nums) else nums[mid]
            
            if nums[mid] == target:
                return mid
            elif nums[first] < nums[mid] and nums[mid] < after:
                first = mid + 1
            elif nums[mid] > after:
                rIndex = mid + 1
            elif nums[mid] < nums[-1] and nums[mid] > before:
                last = mid - 1
            elif nums[mid] < before:
                rIndex = mid

        if target >= nums[rIndex] and target <= nums[-1]:
            first = rIndex
            last = len(nums) - 1
        elif target >= nums[rIndex] and target >= nums[-1]:
            first = 0
            last = rIndex
        elif target < nums[rIndex]:
            return -1
        
        while first <= last:
            mid = first + (last - first) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                last = mid - 1
            else:
                first = mid + 1
        return -1
    
s = Solution()
assert s.search([1], 0) == -1, "#1"
assert s.search([1,3,5], 1) == 0, "#2"
assert s.search([4,5,6,7,0,1,2], 0) == 4, "#3"
assert s.search([4,5,6,7,0,1,2], 3) == -1, "#4"
assert s.search([5,1,3], 5) == 0, "#5"
assert s.search([5,1,2,3,4], 1) == 1, "#6"