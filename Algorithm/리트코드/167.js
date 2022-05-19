/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (numbers, target) {
  const answer = [1, 2];

  let left = 0;
  let right = numbers.length - 1;

  while (left < right) {
    let twoSum = numbers[left] + numbers[right];
    if (twoSum === target) {
      answer[0] = left + 1;
      answer[1] = right + 1;
      break;
    } else if (twoSum < target) {
      left += 1;
    } else {
      right -= 1;
    }
  }

  return answer;
};
