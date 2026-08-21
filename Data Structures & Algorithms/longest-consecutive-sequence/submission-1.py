class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        max_count = 0

        for num in hash_set:
            if num - 1 not in hash_set:
                count = 1
                x = num
                while x + 1 in hash_set:
                    count+=1
                    x += 1
                max_count = max(max_count, count)

        return max_count

            

        