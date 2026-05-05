class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for s in strs:
            sorted_s = tuple(sorted(s))
            if sorted_s not in hash_map:
                hash_map[sorted_s] = []
            hash_map[sorted_s].append(s)
        return [v for v in hash_map.values()]