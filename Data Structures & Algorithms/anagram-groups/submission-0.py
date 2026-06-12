class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group={}
        for word in strs:
            sorted_char= sorted(word)
            key= "".join(sorted_char)
            if key not in group:
                group[key]= []
            group[key].append(word)
        return list(group.values())    

