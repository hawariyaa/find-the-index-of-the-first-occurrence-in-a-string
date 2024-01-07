# in this leet code we are asked to find out if a sub-string name neele is found in
# haystack and if it exists we will check if the first index it appears
# example: haystack = "speeddail" needle = "speed"
# output = 0
# know if needle is empty string we assume it exists inside haystack and return 0
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "": return 0
        for i in range(len(haystack) + 1 - len(needle)):
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    break
                if j == len(needle) -1:
                    return i
        return -1
# this time complexity is 0(n * m)
# space complexity is 0(1)
# there is another way to solve the above problem using the KMP algorithm which is more efficient with
# its time complexity O(n + m) but space complexity will be O(m)
