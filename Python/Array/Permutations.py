class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms, sol = [], []

        def backtracking():
            if len(sol) == len(nums):
                perms.append(sol[:])
                return
            
            for num in nums:
                if num not in sol:
                    sol.append(num)
                    backtracking()
                    sol.pop()
                    
        backtracking()
        return perms
