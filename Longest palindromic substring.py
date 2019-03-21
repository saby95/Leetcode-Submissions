class Solution(object):
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def isPalindrome(s):
            return s==s[::-1]
    
        size = len(s)
        l=0
        longest=""
        long_len=1
        while l<size:
            r=l+long_len
            while r<=size:
                tmp = s[l:r]
                if isPalindrome(tmp) and (len(tmp)>len(longest)):
                    longest=tmp
                    long_len=len(tmp)
                r+=1
            l+=1
        
        return longest

def stringToString(input):
    return input[1:-1].decode('string_escape')

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            s = stringToString(line)
            
            ret = Solution().longestPalindrome(s)

            out = (ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()