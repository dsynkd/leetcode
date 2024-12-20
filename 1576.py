class Solution(object):
    def modifyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        sl = list(s)
        l = len(s)
        for i in range(0, l):
            c = sl[i]
            if(c != '?'): continue
            cl = sl[i-1]
            cr = sl[(i+1)%l]
            for cn in range(97, 122):
                cc = chr(cn)
                if(cc == cl or cc == cr): continue
                sl[i] = cc
                break
        return "".join(sl)
