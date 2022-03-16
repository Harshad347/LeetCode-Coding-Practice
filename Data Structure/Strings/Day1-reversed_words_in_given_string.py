class Solution:
    def reverseWords(self, s: str) -> str:
        # spliting words to list and getting them in reverse order
        res = s.split()[::-1]
        # joining list to string with a space in between elements
        return " ".join(res)
