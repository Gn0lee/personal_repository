/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
var checkInclusion = function (s1, s2) {
  if (s1.length > s2.length) return false;

  let left = 0;
  let right = 0;
  const s1Char = {};
  let requiredChar = s1.length;

  for (let i = 0; i < s1.length; i++) {
    s1Char[s1[i]] = (s1Char[s1[i]] || 0) + 1;
  }

  while (right < s2.length) {
    if (s1Char[s2[right]] > 0) requiredChar--;

    s1Char[s2[right]]--;

    right++;

    if (requiredChar === 0) return true;

    if (right - left === s1.length) {
      if (s1Char[s2[left]] >= 0) requiredChar++;

      s1Char[s2[left]]++;

      left++;
    }
  }

  return false;
};
