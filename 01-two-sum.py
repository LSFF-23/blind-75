class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        checked = dict()
        for i in range(len(nums)):
            try:
                which = target - nums[i]
                return [checked[which][0], i]
            except KeyError:
                if nums[i] in checked:
                    checked[nums[i]].append(i)
                else:
                    checked[nums[i]] = [i]
        return []

s = Solution()
assert s.twoSum([2,7,11,15], 9) == [0,1], "#1"
assert s.twoSum([3,2,4], 6) == [1,2], "#2"
assert s.twoSum([3,3], 6) == [0,1], "#3"
