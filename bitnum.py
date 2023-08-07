N = int(input("N = "))


class Solution:
    def bitnum(self, N):
        count = 0
        i = 0
        for i in (bin(N)[2:]):
            if i == "1":
                count += 1
        return count


obj = Solution()
print(obj.bitnum(N))





