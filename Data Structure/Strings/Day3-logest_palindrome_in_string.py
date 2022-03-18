class Solution:
    def longestPalindrome(self, s: str) -> int:
        # sort string
        s = sorted(s)
        # if length of string is 1, then longest palindrome will be 1
        if(len(s) == 1):
            return 1
        else:
            i, res, odd = 0, 0, 0
            while i < len(s):
                freq = 1
                # count frequency of character
                j = s.count(s[i])
                # for even frequescies
                if j % 2 == 0:
                    res += j
                # for odd frequencies
                elif j % 2 == 1 and j > 2:
                    # one odd frequency to keep at middle
                    odd = 1
                    res += j-1
                else:
                    odd = 1
                # spliting visited charracter
                i = i+j

        return res+odd
