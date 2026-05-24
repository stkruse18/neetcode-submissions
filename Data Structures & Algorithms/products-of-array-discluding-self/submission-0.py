class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = 0
        total = 1
        cow = [0] * len(nums)
        for num in nums:
            if num == 0:
                zeros += 1
            else:
                total = total * num
        if zeros >= 2:
            return cow
        elif zeros == 1:
            for idx, num in enumerate(nums):
                if num == 0:
                    cow[idx] = total
                    return cow
        else:
            for idx, num in enumerate(nums):
                cow[idx] = total//num
        return cow
