/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function (s) {
  const answer = [];
  const sList = s.split(" ");

  for (let word of sList) {
    let left = 0;
    let right = word.length;
    let wordList = [...word];

    while (left < right) {
      let tmp = wordList[left];
      wordList[left] = wordList[right];
      wordList[right] = tmp;
      left += 1;
      right -= 1;
    }

    answer.push(wordList.join(""));
  }

  return answer.join(" ");
};
