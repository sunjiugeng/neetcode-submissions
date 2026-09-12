class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = {}
        hash_t = {}
        for s_c in s:
            hash_s[s_c] = hash_s[s_c] + 1 if s_c in hash_s else 1
        for t_c in t:
            hash_t[t_c] = hash_t[t_c] + 1 if t_c in hash_t else 1
        return hash_s == hash_t