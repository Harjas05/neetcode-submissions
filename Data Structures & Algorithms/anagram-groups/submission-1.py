class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # output is list of lists 
        # "act","pots","tops","cat","stop","hat"
        # [["hat"],["act", "cat"],["stop", "pots", "tops"]]

        # frequency of characters 

        # hash_map
        # base angram: [list of anagrams]
        hash_map = {}
        for str in strs:
            sortword = "".join(sorted(str))
            if sortword not in hash_map:
                hash_map[sortword] = []
            hash_map[sortword].append(str)
        
        results = []
        for h in hash_map:
            results.append(hash_map[h])
        return results


            



        