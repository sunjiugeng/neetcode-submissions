class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return get_hash(s) == get_hash(t)

def get_hash(string: str) -> dict:
        table = {}
        for s in string:
            table[s] = table[s] + 1 if s in table else 1
        return table
