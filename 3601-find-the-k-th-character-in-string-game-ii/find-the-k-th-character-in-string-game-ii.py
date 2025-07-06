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
'''
Every operation doubles the string word 
p is the largest power of 2 we can subtract from the kth element of word
k - p gives us the element that the kth element depended on in the previous operation.
If the (k - p)th element is the same as kth element, operation == 0. 
If (k - p)th element is different, it will be the previous letter in the alphabet.
Count how many times (k - p)th element is the previous letter in the alphabet
'''