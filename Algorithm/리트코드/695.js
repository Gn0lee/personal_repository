/**
 * @param {number[][]} grid
 * @return {number}
 */

const bfs = (y, x, grid) => {
  let dy = [-1, 0, 1, 0];
  let dx = [0, 1, 0, -1];
  let q = [[y, x]];
  let tmp = 0;

  grid[y][x] = 0;

  while (q.length) {
    let [nowY, nowX] = q.shift();

    tmp += 1;

    for (let i = 0; i < 4; i++) {
      let newY = dy[i] + nowY;
      let newX = dx[i] + nowX;

      if (
        0 <= newY &&
        newY < grid.length &&
        0 <= newX &&
        newX < grid[0].length &&
        grid[newY][newX] === 1
      ) {
        grid[newY][newX] = 0;
        q.push([newY, newX]);
      }
    }
  }

  return tmp;
};

const dfs = (y, x, grid) => {
  if (
    0 > y ||
    y >= grid.length ||
    0 > x ||
    x >= grid[0].length ||
    grid[y][x] === 0
  )
    return 0;
  grid[y][x] = 0;

  return (
    1 +
    dfs(y + 1, x, grid) +
    dfs(y - 1, x, grid) +
    dfs(y, x + 1, grid) +
    dfs(y, x - 1, grid)
  );
};

var maxAreaOfIsland = function (grid) {
  let m = grid.length;
  let n = grid[0].length;

  let answer = 0;

  for (let y = 0; y < m; y++) {
    for (let x = 0; x < n; x++) {
      // if(grid[y][x] === 1){
      //     let currArea = bfs(y,x,grid);
      //     answer = Math.max(answer, currArea);
      // }
      answer = Math.max(answer, dfs(y, x, grid));
    }
  }

  return answer;
};
