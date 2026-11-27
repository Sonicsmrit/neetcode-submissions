class Solution:

    def encode(self, strs: List[str]) -> str:
        vals = []
        for val in strs:
            leng =  len(val)

            vals.append(f"{leng}#{val}")

        return "".join(vals)
        

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])

            val = s[j+1:j+1+length]

            res.append(val)

            i = length+1+j

        return res
        
    

