class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        Sum = 0
        last_val = 0
        for i in range(len(s)):
            if (dic[s[i]] in [1,10,100]) and (last_val not in [1,10,100]):
                Sum = Sum + dic[s[i]]
            elif (last_val in [1,10,100]) and (last_val<dic[s[i]]):
                Sum = Sum + dic[s[i]] - (2*last_val)
            else:
                Sum = Sum + dic[s[i]]
            last_val = dic[s[i]]
        return Sum

def stringToString(input):
    return input[1:-1].decode('string_escape')

def intToString(input):
    if input is None:
        input = 0
    return str(input)

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
            
            ret = Solution().romanToInt(s)

            out = intToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()