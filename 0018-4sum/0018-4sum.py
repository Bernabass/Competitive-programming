class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = set()

        nums.sort()
        n = len(nums)

        def two_sum(idx, target):
            ans = []
            info = {}
            for i in range(idx, len(nums)):
                val = nums[i]
                if target - val in info:
                    ans.append([info[target - val], i])

                info[val] = i

            return ans

        for i in range(n):
            for j in range(i+1, n):
                s = target - (nums[i] + nums[j])
                pair = two_sum(j+1, s)

                if pair:
                    for k, l in pair:
                        ans.add((nums[i], nums[j], nums[k], nums[l]))

        return ans