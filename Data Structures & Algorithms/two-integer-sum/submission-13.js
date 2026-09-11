class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
     const indices ={}
     nums.forEach((num,i)=>indices[num]=i)
     console.log(indices)
    
    for(let i=0;i<nums.length;i++){
        const remainder = target-nums[i];
        if(indices[remainder] !=undefined && indices[remainder]!==i){
            return [Math.min(i,indices[remainder]),Math.max(i,indices[remainder])]
        }
    }
    return []
}
}
