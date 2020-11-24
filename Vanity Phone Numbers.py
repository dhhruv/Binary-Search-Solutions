class Solution:
    def solve(self, digits):
        d = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        ls = list(d.get(digits[0]))
        temp = []
        for i in range(1, len(digits)):
            temp = sorted(ls * len(d.get(digits[i])))
            c2 = 0
            while c2 != len(temp):
                for j in range(len(d.get(digits[i]))):
                    c1 = 0
                    while c1 != len(d.get(digits[i])):
                        if c2 == len(temp):
                            break
                        temp[c2] += d.get(digits[i])[c1]
                        c1 += 1
                        c2 += 1
            ls = temp
        return ls