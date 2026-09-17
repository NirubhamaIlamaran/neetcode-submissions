class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        encoded_string=""
        for i in range(0,len(strs)):
            encoded_string+=str(len(strs[i]))+"#"+strs[i]
        return encoded_string

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        n = len(s)
        while i < n:
            h = s.find('#', i)
            L = int(s[i:h])
            i = h + 1
            res.append(s[i : i + L])
            i += L
        return res
        
