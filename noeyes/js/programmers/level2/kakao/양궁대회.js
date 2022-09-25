function solution(n, info) {
  const answer = [];

  function checkResult(result) {
    let aSum = 0;
    let lSum = 0;

    for (let i = 0; i < result.length; i++) {
      if (result[i] > info[i]) {
        lSum += 10 - i;
      } else {
        aSum += 10 - i;
      }
    }

    return lSum - aSum;
  }

  function findMax(result) {
    const max = 0;

    for (let i = 0; i < result.length; i++) {
      if (result[i] > result[max]) {
        max = i;
      }
    }

    return max;
  }

  function calcLion() {
    let lionArrow = n;
    const result = Array(11).fill(0);

    for (let i = 0; i < info.length; i++) {
      if (lionArrow - info[i] >= 1) {
        result[i] = info[i] + 1;
        lionArrow -= info[i] + 1;
      }
    }

    if (lionArrow > 0) {
      result[0] += lionArrow;
      lionArrow = 0;
    }

    // answer.push(result.push(checkResult(result)));

    return result;
  }
  return calcLion();
}
// [3,3,3,2,2,2]
// [4,4,4,3,0,0];
console.log(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]));
// [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1] 7 3 2 1 0= 13
// [1, 1, 2, 0, 1, 2, 2, 0, 0, 0, 0] 10 9 8 6 5 4 = 42

// 20
