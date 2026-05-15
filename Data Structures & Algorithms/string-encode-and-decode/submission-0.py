class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for i in strs:
            encoded += i
            encoded += "#"
        
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:

        decoded = []

        j = 0

        for i in range(len(s)):
            if s[i] == '#' and (i == len(s)-1 or s[i+1] != '#'):
                decoded.append(s[j:i])
                j = i+1 
            
                

        return decoded