class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        vocab = {}
        
        for w1 in strs:

            val = sorted(w1)
            val = "".join(val)
            group = vocab.get(val,[])

            group.append(w1)
            vocab[val] = group 

        return list(vocab.values())

        
                 