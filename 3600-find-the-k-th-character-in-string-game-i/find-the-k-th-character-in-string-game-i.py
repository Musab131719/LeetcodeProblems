class Solution:
    def kthCharacter(self, k: int) -> str:
        count = 0
        while k != 1:
            n = ceil(math.log(k, 2)) - 1
            p = 2 ** n
            k -= p
            count += 1
        # 97 is unicode for 'a'
        return chr(97 + count)