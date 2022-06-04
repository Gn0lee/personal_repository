/**
 * @param {number[][]} image
 * @param {number} sr
 * @param {number} sc
 * @param {number} newColor
 * @return {number[][]}
 */
var floodFill = function (image, sr, sc, newColor) {
  const oldColor = image[sr][sc];
  const m = image.length;
  const n = image[0].length;
  const visited = new Array(m).fill(0).map((elem) => new Array(n).fill(false));
  const dy = [-1, 0, 1, 0];
  const dx = [0, 1, 0, -1];
  const q = [[sr, sc]];

  while (q.length) {
    let [nowY, nowX] = q.shift();
    visited[nowY][nowX] = true;
    image[nowY][nowX] = newColor;

    for (let i = 0; i < 4; i++) {
      let newY = dy[i] + nowY;
      let newX = dx[i] + nowX;

      if (
        0 <= newY &&
        newY < m &&
        0 <= newX &&
        newX < n &&
        !visited[newY][newX] &&
        image[newY][newX] === oldColor
      ) {
        q.push([newY, newX]);
      }
    }
  }

  return image;
};
