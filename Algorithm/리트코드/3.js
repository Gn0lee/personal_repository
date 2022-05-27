/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function (s) {
  if (s.length === 0) return 0;

  const sMap = new Map();
  const sList = [...s];
  let answer = 1;
  let left = 0;
  let right = 0;

  while (right < sList.length) {
    if (sMap.has(sList[right])) {
      left = Math.max(left, sMap.get(sList[right]) + 1);
    }
    answer = Math.max(answer, right - left + 1);
    sMap.set(sList[right], right);
    right += 1;
  }

  return answer;
};
