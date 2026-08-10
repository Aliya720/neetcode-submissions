class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t): return False
        
        hash_map = {}
        for ch in s:
            hash_map[ch] = hash_map.get(ch,0) + 1
        
        for ch in t:
            if ch not in hash_map:
                return False
            else :
                if hash_map[ch] == 0:
                    return False
                else:
                    hash_map[ch] -= 1

        return True