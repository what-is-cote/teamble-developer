function solution(n, lost, reserve) {
  let count = n - lost.length;
  reserve
    .filter((e) => {
      if (lost.includes(e)) {
        lost[lost.indexOf(e)] = -2;
        count += 1;
        return false;
      }
      return true;
    })
    .sort((a, b) => a - b)
    .forEach((stu) => {
      if (lost.includes(stu - 1)) {
        lost[lost.indexOf(stu - 1)] = -2;
        count += 1;
      } else if (lost.includes(stu + 1)) {
        lost[lost.indexOf(stu + 1)] = -2;
        count += 1;
      }
    });

  return count;
}

console.log(solution(5, [6, 5, 3, 2], [2, 5, 6, 4]));
