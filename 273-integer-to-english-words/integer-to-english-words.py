class Solution(object):
    def numberToWords(self, num):
        if num == 0:
            return "Zero"    
        
        units = {"0":"", "1": "One", "2": "Two", "3": "Three", "4": "Four", "5": "Five", "6": "Six", "7": "Seven", "8": "Eight", "9": "Nine"}
        tens = {"0":"", "1": "Ten","2": "Twenty", "3": "Thirty", "4": "Forty", "5": "Fifty", "6": "Sixty", "7": "Seventy", "8": "Eighty", "9": "Ninety"}
        teens = {"10":"Ten", "11": "Eleven", "12": "Twelve", "13": "Thirteen", "14": "Fourteen", "15": "Fifteen", "16": "Sixteen", "17": "Seventeen", "18": "Eighteen", "19": "Nineteen"}
        suffix = {1:"", 2:"Thousand", 3:"Million", 4:"Billion"}

        num_list = [x for x in str(num)]
        original_reverse = str(num)[::-1]
        reverse = num_list[::-1]
        n = len(num_list)
        result = ""

        for i in range(n):
            digit = reverse[i]
            if i % 3 == 0:
                reverse[i] = units[digit] 
            elif i % 3 == 2:
                if units[digit] is not "":
                    reverse[i] = units[digit] + " Hundred"
                else:
                    reverse[i] = ""
            else:
                prev = original_reverse[i-1] if i > 0 else "0"
                if digit == "1" and reverse[i-1] != "0":
                    reverse[i] = teens[digit + prev]
                    reverse[i-1] = ""
                else:
                    reverse[i] = tens[digit]
        
        flip = reverse[::-1]
        first_group = n % 3 or 3
        groups = []
        groups.append(" ".join([x for x in flip[:first_group] if x != ""]).strip())
        
        for i in range(first_group, n, 3):
            groups.append(" ".join([x for x in flip[i:i+3] if x != ""]).strip())

        for i in range(len(groups)): 
            if groups[i] is not "":   
                groups[i] = groups[i] + " " + suffix[len(groups) - i]

        for group in groups:
            if group is not "":
                result += " " + group
        return result.strip()