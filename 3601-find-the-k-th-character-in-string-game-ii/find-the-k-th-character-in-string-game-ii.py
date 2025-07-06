class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        count = 0
        while k != 1:
            n = ceil(math.log(k, 2)) - 1
            p = 2 ** n
            k -= p            
            if operations[n]:
                count += 1
        return chr(97 + count % 26)