class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for index,num in enumerate(nums):
            hmap[num] = index

        for index,num in enumerate(nums):
            number_to_check = target-num
            # if num != number_to_check:
            if number_to_check in hmap and  hmap[number_to_check] !=index:
                    return [index,hmap[number_to_check]]
        
        return []

            
        