/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function (nums) {
  let curr = 0;
  let end = 0;

  while (curr < nums.length) {
    if (nums[curr] != 0) {
      nums[end] = nums[curr];
      end += 1;
      curr += 1;
    } else {
      curr += 1;
    }
  }

  // console.log(nums, curr, end)

  for (let i = end; i < nums.length; i++) {
    nums[i] = 0;
  }
};
