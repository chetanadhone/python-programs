class Solution(object):
    def groupAnagrams(self, strs):
        groups = {}
        for string in strs:
            key = "".join(sorted(string)) #join takes list and converts it to a string
            if key in groups:
                groups[key].append(string)
            else:
                groups[key] = [string]
        return list(groups.values())
a = "abc"
print([a])
# print((sorted("abc",reverse=True))) #sorts desceding
