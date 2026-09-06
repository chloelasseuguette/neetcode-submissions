class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_list = []
        c = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if nums[i] + nums[j] == target:
                        target_list.append(i)
                        target_list.append(j)
                        target_list.sort()
                        return target_list