from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        amap=defaultdict(list)
        for i in strs:
            key="".join(sorted(i))
            amap[key].append(i)
        return list(amap.values())

        