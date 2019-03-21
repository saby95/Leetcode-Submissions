class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height)==0:
            return 0
        st=0
        en=len(height)-1
        cap=0
        while(st<en):
            if(height[st]>height[en]):
                if(height[en]*(en-st)) > cap:
                    cap = height[en]*(en-st)
                en -= 1
            else:
                if(height[st]*(en-st)) > cap:
                    cap = height[st]*(en-st)
                st += 1
            
        return cap

def stringToIntegerList(input):
    return json.loads(input)

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
            height = stringToIntegerList(line)
            
            ret = Solution().maxArea(height)

            out = intToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()