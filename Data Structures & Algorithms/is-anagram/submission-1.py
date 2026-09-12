class Solution:
    def get_hash(self, string: str) -> dict:
        table = {}
        for s in string:
            table[s] = table[s] + 1 if s in table else 1
        return table
    def isAnagram(self, s: str, t: str) -> bool:
        return self.get_hash(s) == self.get_hash(t)
