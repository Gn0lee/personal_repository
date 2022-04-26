/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
 var rotate = function(nums, k) {
    let left = 0;
    let right = nums.length - 1;
    k %= nums.length;
    
    const reverse = (l,r) => {
        while(l <= r){
            let tmp = nums[l];
            nums[l] = nums[r];
            nums[r] = tmp
            l += 1;
            r -= 1;
        }
    }
    
    reverse(0,right);
    reverse(0,k-1);
    reverse(k,right);
};