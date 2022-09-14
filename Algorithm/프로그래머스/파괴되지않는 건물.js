function worngSolution(board, skill) {
  let answer = board.length * board[0].length;

  skill.forEach((el) => {
    const [type, r1, c1, r2, c2, degree] = el;

    for (let m = c1; m <= c2; m++) {
      for (let n = r1; n <= r2; n++) {
        if (type === 1) {
          let result = board[n][m] - degree;
          if (board[n][m] > 0 && result < 1) answer -= 1;
          board[n][m] = result;
        } else {
          let result = board[n][m] + degree;
          if (board[n][m] < 1 && result > 0) answer += 1;
          board[n][m] = result;
        }
      }
    }
  });
  return answer;
}

function solution2(board, skill) {
  let answer = 0;
  const tmp = new Array(board.length + 1)
    .fill(0)
    .map((el) => new Array(board[0].length + 1).fill(0));

  skill.forEach((el) => {
    const [type, r1, c1, r2, c2, degree] = el;

    if (type === 1) {
      tmp[r1][c1] -= degree;
      tmp[r1][c2 + 1] += degree;
      tmp[r2 + 1][c1] += degree;
      tmp[r2 + 1][c2 + 1] -= degree;
    } else {
      tmp[r1][c1] += degree;
      tmp[r1][c2 + 1] -= degree;
      tmp[r2 + 1][c1] -= degree;
      tmp[r2 + 1][c2 + 1] += degree;
    }
  });

  for (let m = 0; m < board.length + 1; m++) {
    for (let n = 0; n < board[0].length; n++) {
      tmp[m][n + 1] += tmp[m][n];
    }
  }

  for (let n = 0; n < board[0].length + 1; n++) {
    for (let m = 0; m < board.length; m++) {
      tmp[m + 1][n] += tmp[m][n];
    }
  }

  for (let m = 0; m < board.length; m++) {
    for (let n = 0; n < board[0].length; n++) {
      if (board[m][n] + tmp[m][n] > 0) answer += 1;
    }
  }

  return answer;
}

function solution(board, skill) {
  let answer = 0;
  const tmp = Array.from(Array(board.length + 1), () =>
    Array(board[0].length + 1).fill(0)
  );

  skill.forEach((el) => {
    const [type, r1, c1, r2, c2, degree] = el;

    if (type === 1) {
      tmp[r1][c1] -= degree;
      tmp[r1][c2 + 1] += degree;
      tmp[r2 + 1][c1] += degree;
      tmp[r2 + 1][c2 + 1] -= degree;
    } else {
      tmp[r1][c1] += degree;
      tmp[r1][c2 + 1] -= degree;
      tmp[r2 + 1][c1] -= degree;
      tmp[r2 + 1][c2 + 1] += degree;
    }
  });

  for (let m = 0; m < board.length + 1; m++) {
    for (let n = 0; n < board[0].length; n++) {
      tmp[m][n + 1] += tmp[m][n];
    }
  }

  for (let n = 0; n < board[0].length + 1; n++) {
    for (let m = 0; m < board.length; m++) {
      tmp[m + 1][n] += tmp[m][n];
    }
  }

  for (let m = 0; m < board.length; m++) {
    for (let n = 0; n < board[0].length; n++) {
      if (board[m][n] + tmp[m][n] > 0) answer += 1;
    }
  }

  return answer;
}
