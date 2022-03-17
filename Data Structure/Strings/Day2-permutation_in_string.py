class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        # getting permutaions of second string
        for i in range(len(s2)-len(s1)+1):
            # getting permutations of same length as first string and sort it
            s3 = sorted(s2[i:i+len(s1)])
            if s3 == s1:
                return True

        return False
