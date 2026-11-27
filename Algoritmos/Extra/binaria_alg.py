"""
BUSCA BINÁRIA (LEETCODE #704)
Exemplo baseado no print para o array: [-1, 0, 3, 5, 9, 12]
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m

        return -1


# -----------------------------------------------------------------------------
# TESTE COM: [-1, 0, 3, 5, 9, 12]
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    sol = Solution()
    nums = [-1, 0, 3, 5, 9, 12]

    print(f"Array: {nums}\n")
    print(f"Buscando target = 9  -> índice: {sol.search(nums, 9)}")
    print(f"Buscando target = 2  -> índice: {sol.search(nums, 2)} (não encontrado)")
