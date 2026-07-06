class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
                nums.sort()
                closest = float('inf')
                result = 0
                for i in range(len(nums) - 2):
                    left, right = i + 1, len(nums) - 1
                    while left < right:
                        total = nums[i] + nums[left] + nums[right]

                        if abs(target - total) < closest:
                            closest = abs(target - total)
                            result = total
                        if total < target:
                            left += 1
                        elif total > target:
                            right -= 1
                        else:
                            return total
                return result