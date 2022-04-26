/**
 * @param {number[]} nums
 * @return {number[]}
 */
 var sortedSquares = function(nums) {
    if(nums.length === 1){
        return [Math.pow(nums[0],2)];
    }
    
    const answer = [];
    let first = nums[0];
    let last = nums[nums.length - 1];
    
    if(first < 0 && last < 0){
        for(let i = nums.length - 1; i > -1; i--){
            answer.push(Math.pow(nums[i],2));
        }
    }else if(first > 0 && last > 0){
        for(let i = 0; i < nums.length ; i++){
            answer.push(Math.pow(nums[i],2));
        }
    }else if(first < 0 && last === 0){
        answer.push(0);
        for(let i = nums.length - 2; i > -1; i--){
            answer.push(Math.pow(nums[i],2));
        }
    }else if(first === 0 && last > 0){
        answer.push(0);
        for(let i = 1; i < nums.length ; i++){
            answer.push(Math.pow(nums[i],2));
        }
    }else{
        let left = 0;
        let right = nums.length - 1;
        let mid;
        while(left <= right){
            mid = Math.floor((left + right) / 2);
            if(nums[mid] === 0){
                break;
            }else if(nums[mid] > 0){
                right = mid - 1;
            }else{
                left = mid + 1;
            }
        }
    
        if(nums[mid] === 0){
            left = mid -1;
            right = mid + 1;
            answer.push(0);
        }else{
            let tmp = left;
            left = right;
            right = tmp;
        }
    
        while(0 <= left || right < nums.length){
            if(left < 0){
                answer.push(Math.pow(nums[right],2));
                right += 1;
            }else if(right >= nums.length){
                answer.push(Math.pow(nums[left],2));
                left -= 1;
            }else if(Math.abs(nums[left]) < Math.abs(nums[right])){
                answer.push(Math.pow(nums[left],2));
                left -= 1;
            }else if(Math.abs(nums[left]) > Math.abs(nums[right])){
                answer.push(Math.pow(nums[right],2));
                right += 1;
            }else{
                answer.push(Math.pow(nums[left],2));
                answer.push(Math.pow(nums[right],2));
                left -= 1;
                right += 1;
            }
        }
    }
    
    return answer
};