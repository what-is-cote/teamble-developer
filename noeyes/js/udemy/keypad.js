function solution(numbers, hand) {
  var leftOnly = [1, 4, 7];
  var rightOnly = [3, 6, 9];
  var nearst = [2, 5, 8, 0];
  var lp = [3, 0];
  var rp = [3, 2];

  return numbers
    .map((n) => {
      if (leftOnly.includes(n)) {
        lp[0] = leftOnly.indexOf(n);
        lp[1] = 0;
        return "L";
      } else if (rightOnly.includes(n)) {
        rp[0] = rightOnly.indexOf(n);
        rp[1] = 2;
        return "R";
      } else if (nearst.includes(n)) {
        const lDistance =
          Math.abs(lp[0] - nearst.indexOf(n)) + Math.abs(lp[1] - 1);
        const rDistance =
          Math.abs(rp[0] - nearst.indexOf(n)) + Math.abs(rp[1] - 1);

        if (lDistance === rDistance) {
          if (hand === "right") {
            rp[0] = nearst.indexOf(n);
            rp[1] = 1;
            return "R";
          } else {
            lp[0] = nearst.indexOf(n);
            lp[1] = 1;
            return "L";
          }
        } else if (lDistance < rDistance) {
          lp[0] = nearst.indexOf(n);
          lp[1] = 1;
          return "L";
        } else {
          rp[0] = nearst.indexOf(n);
          rp[1] = 1;
          return "R";
        }
      }
    })
    .join("");
}

console.log(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"));
