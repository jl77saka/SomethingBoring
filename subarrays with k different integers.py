class Solution:
    def subarraysWithKDistinct(self, nums, k):
        subWithMaxK = self.subarrayWithAtMostK(nums, k)
        reducedSubWithMaxK = self.subarrayWithAtMostK(nums, k - 1)
        return subWithMaxK - reducedSubWithMaxK
    
    def subarrayWithAtMostK(self, nums, k):
        count_map = {}
        left = 0
        ans = 0
        
        for right in range(len(nums)):
            count_map[nums[right]] = count_map.get(nums[right], 0) + 1
            
            while len(count_map) > k:
                count_map[nums[left]] -= 1
                if count_map[nums[left]] == 0:
                    del count_map[nums[left]]
                left += 1
                
            ans += right - left + 1  # Size of subarray
        
        return ans
