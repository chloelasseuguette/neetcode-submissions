class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        flag = False
        no_dupe_set = set()
        for i in range(len(nums)):
            no_dupe_set.add(nums[i])
        if len(nums) != len(no_dupe_set):
            flag = True
        return flag
