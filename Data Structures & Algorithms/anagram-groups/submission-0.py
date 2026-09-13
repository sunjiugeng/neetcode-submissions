class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_anagrams = {}
        for string in strs:
            sorted_str = ''.join(sorted(string))
            if sorted_str in group_anagrams:
                group_anagrams[sorted_str].append(string)
            else:
                group_anagrams[sorted_str] = [string]
        return [group_anagrams[g] for g in group_anagrams]