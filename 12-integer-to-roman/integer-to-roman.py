class Solution(object):
    def intToRoman(self, num):

        n = len(str(num))   # Determines no. of digits 
        count = [int(x) for x in str(num)]
        symbols = {1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M"}
        dict_9 = {"C":"CM", "X":"XC", "I":"IX"}
        dict_4 = {"C":"CD", "X":"XL", "I":"IV"}
        dict_5 = {"C":"D", "X":"L", "I":"V"}
        result = [""] * 4

        while len(count) < 4:
            count.insert(0,0)

        for i in range(4):
            if count[i] == 0:
                continue
            while count[i] is not 0:
                result[i] += symbols[10**(4-i-1)]
                count[i] -= 1

        for i in range(1,4):
            if len(result[i]) == 9:
                result[i] = dict_9[symbols[10**(4-i-1)]]
            elif len(result[i]) == 4:
                result[i] = dict_4[symbols[10**(4-i-1)]]
            elif len(result[i]) >= 5:
                result[i] = dict_5[symbols[10**(4-i-1)]] + result[i][:-5]
        
        return "".join(result)