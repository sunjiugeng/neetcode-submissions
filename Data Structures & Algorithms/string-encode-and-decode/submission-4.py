class Solution:

    def encode(self, strs: List[str]) -> str:
        return 'None' if len(strs) == 0 else "ü".join(strs)
    def decode(self, s: str) -> List[str]:
        return s.split("ü") if s != 'None' else []