class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)

        for s in strs:
            tmp = sorted(s)
            hm[tuple(tmp)].append(s)

        # print(list(hm.values()))
        return list(hm.values())
        