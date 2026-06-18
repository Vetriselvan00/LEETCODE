class Solution(object):
    def processStr(self, s, k):
        stack = []
        rev = 0

        for i in range(len(s)):
            if 'a' <= s[i] <= 'z':
                rev += 1

            elif s[i] == '#':
                rev *= 2

            elif s[i] == '%':
                pass

            elif s[i] == '*':
                if rev > 0:
                    rev -= 1

            stack.append(rev)

        if k >= rev:
            return '.'

        for i in range(len(s) - 1, -1, -1):
            z = stack[i - 1] if i > 0 else 0

            if 'a' <= s[i] <= 'z':
                if k == z:
                    return s[i]

            elif s[i] == '#':
                if k >= z:
                    k -= z

            elif s[i] == '%':
                k = rev - 1 - k

            elif s[i] == '*':
                pass

            rev = z

        return '.'
