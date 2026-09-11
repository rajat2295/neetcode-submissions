class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs){
        let indices = {}
        const final =[]
        const newStr = strs.map(str=>str.split('').sort().join(''))
        newStr.forEach((str,i)=>{
            if(indices[str]==undefined)
             indices[str]= [i]
             else{
               indices[str].push(i) 
             }
        })
        Object.values(indices).forEach(val=>{
               const sub =[]
            val.forEach(index=>sub.push(strs[index]))
            final.push(sub)
        })
     
        // newStr.forEach((str,i)=>{
        //     const baseWord = str.split('').sort().join('')
        //     if(indices[baseWord]!=undefined
        // })
        return final
    }
}
