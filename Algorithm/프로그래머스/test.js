const codeOwners = {
  scripts: ["배수진"],
  services: {
    "business-ledger": ["고찬균, 배수진"],
    "toss-card": ["채주민", "유재섭"],
    payments: ["유재섭"],
  },
};

/*
 * `codeOwnersMap`과 `directory`를 입력받아
 * `directory`의 코드 주인 목록을 반환하는 함수를 작성하세요.
 */
function solution(codeOwnersMap, directory) {
  const directoryList = directory.split("/");

  let currMap = codeOwnersMap;

  directoryList.forEach((el) => {
    currMap = currMap[el];
  });

  // console.log(currMap)
  return currMap;
}

console.log(solution(codeOwners, "scripts"));
