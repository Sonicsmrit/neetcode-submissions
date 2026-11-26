class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dic = {}

        for i in strs:
            val = sorted(i)
            val = "".join(val)
            
            group = dic.get(val, [])
            group.append(i)
            dic[val] = group
    
        return list(dic.values())
        

        
                 