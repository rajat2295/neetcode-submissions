class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs){
        let map = {}
        strs.forEach((str)=>{
        const newStr = str.split('').sort().join('')
            if(map[newStr]==undefined)
             map[newStr]= [str]
             else{
               map[newStr].push(str) 
             }
        })
        return Object.values(map)
        // newStr.forEach((str,i)=>{
        //     const baseWord = str.split('').sort().join('')
        //     if(indices[baseWord]!=undefined
        // })
        return final
    }
}
