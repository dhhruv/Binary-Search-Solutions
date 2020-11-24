"""
Intuition
We take the word with minimum length and then check until the prefixes don't match in all the words.
"""
class Solution:
    def solve(self, words):
        st = ""
        temp = ""
        mi = min(words)
        for i in mi:
            temp += i
            for j in words:
                if temp not in j:
                    return st
            st = temp
        return st