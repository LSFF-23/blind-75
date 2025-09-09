class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        segments = []
        segStart = 0
        firstNegative = -1
        lastNegative = -1
        negativeCount = 0
        product = nums[0]

        for i in range(len(nums)):
            if nums[i] < 0 and firstNegative == -1:
                firstNegative = lastNegative = i
                negativeCount += 1
            elif nums[i] < 0 and firstNegative != -1:
                lastNegative = i
                negativeCount += 1
            elif nums[i] == 0:
                segments.append({"start": segStart, "end": i, "fn": firstNegative, "ln": lastNegative, "nc": negativeCount})
                firstNegative = lastNegative = -1
                negativeCount = 0
                segStart = i + 1
            if nums[i] > product:
                product = nums[i]
        
        if segStart < len(nums):
            segments.append({"start": segStart, "end": len(nums), "fn": firstNegative, "ln": lastNegative, "nc": negativeCount})

        for seg in segments:
            if seg["nc"] % 2 == 0:
                curProduct = 1
                for i in range(seg["start"], seg["end"]):
                    curProduct *= nums[i]
                if seg["start"] < seg["end"] and curProduct > product:
                    product = curProduct
            else:
                fnLeft = fnRight = lnLeft = lnRight = 1
                for i in range(seg["start"], seg["end"]):
                    if i >= seg["start"] and i < seg["fn"]:
                        fnLeft *= nums[i]
                    if i > seg["fn"] and i < seg["end"]:
                        fnRight *= nums[i]
                    if i >= seg["start"] and i < seg["ln"]:
                        lnLeft *= nums[i]
                    if i > seg["ln"] and i < seg["end"]:
                        lnRight *= nums[i]
                if seg["start"] < seg["fn"] and fnLeft > product: product = fnLeft 
                if seg["fn"] + 1 < seg["end"] and fnRight > product: product = fnRight
                if seg["start"] < seg["ln"] and lnLeft > product: product = lnLeft
                if seg["ln"] + 1 < seg["end"] and lnRight > product: product = lnRight
        
        return product

s = Solution()
assert s.maxProduct([2,3,-2,4]) == 6, "#1"
assert s.maxProduct([-2,0,-1]) == 0, "#2"
assert s.maxProduct([-2,3,-4]) == 24, "#3"
assert s.maxProduct([0,2]) == 2, "#4"
assert s.maxProduct([0]) == 0, "#5"
assert s.maxProduct([-1,-1]) == 1, "#6"
assert s.maxProduct([-2,0]) == 0, "#7"