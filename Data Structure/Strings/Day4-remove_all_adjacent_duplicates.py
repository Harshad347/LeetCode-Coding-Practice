class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            # if empty then push element
            if len(stack) == 0:
                stack.append(s[i])
            # check if current element is same as the element we just pushed
            elif stack[-1] == s[i]:
                # remove that element from stack and move on
                stack.pop()
            else:
                # if not same then push that element to stack
                stack.append(s[i])

        return ''.join(stack)
