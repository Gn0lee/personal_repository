function chkPrime(x) {
  if (x === "1") return false;

  for (let i = 2; i <= Math.sqrt(Number(x)); i++) {
    if (x % i === 0) return false;
  }
  return true;
}

function solution(n, k) {
  let answer = 0;

  n.toString(k)
    .split("0")
    .forEach((el) => {
      if (el !== "" && chkPrime(el)) answer += 1;
    });

  return answer;
}
