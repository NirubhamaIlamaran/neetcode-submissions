from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        amap=defaultdict(list)
        for i,n in enumerate(nums):
            key=n
            amap[key].append(i)
        li=[]
        for i in set(nums):
            li.append((len(amap[i]),i))
        sortedli=sorted(li)
        return [pair[1] for pair in sortedli[-k:]]
            
        
        