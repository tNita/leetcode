class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data: Dict[str, List[str]] = {}
        for x in strs:
            key = "".join(sorted(x))
            if key in data:
                data[key].append(x)
            else:
                data[key] = [x]
        return [v for v in data.values()]
