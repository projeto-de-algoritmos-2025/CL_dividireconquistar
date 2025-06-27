class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Ordena a lista em ordem crescente. Ex: nums = [3, 2, 1, 5, 6, 4] -> sorted(nums) = [1, 2, 3, 4, 5, 6]
        return sorted(nums)[-k]
