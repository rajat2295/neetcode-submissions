class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        hash_map = {}
        for ele in s :
            hash_map[ele] = hash_map.get(ele,0) + 1
        print(hash_map)
        for ele in t:
            if ele not in hash_map: 
                return False
            hash_map[ele] =  hash_map.get(ele) - 1
            print(hash_map.get(ele))
            if(hash_map.get(ele)) <0 :
                return False
            if(hash_map[ele]==0):
                del hash_map[ele]
        return len(hash_map) == 0



