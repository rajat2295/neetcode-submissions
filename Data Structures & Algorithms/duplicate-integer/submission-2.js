class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const uniqueSet = new Set(nums);
        console.log(nums,uniqueSet,nums.length, uniqueSet.length)
        return nums.length != uniqueSet.size;
size}
}
