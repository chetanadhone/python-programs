# s = input("s = ")
# # s == "".join(sorted(s))
#
# s = list(s)
# print(sorted(s))
# print(s)

class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t): #madam= 5, mads= 3
            return False

        repetition = [0] * 26
        for i in range(len(s)): #i in 5, m
            repetition[ord(s[i]) - ord('a')] += 1 #
            repetition[ord(s[i]) - ord('a')] -= 1
        for i in range(len(repetition)):
            if repetition[i] != 0:
                return False
        return True
obj = Solution()
print(obj.isAnagram("madam", "mads"))
