function solution(s) {
  let count = 0;
  let zero = 0;

  function removeZero(s) {
    for (let c of s) {
      if (c === "0") zero += 1;
    }
    return s.replaceAll("0", "");
  }

  function toBinary(n) {
    let m = n;
    const result = [];
    while (m > 0) {
      result.push((m % 2) + "");
      m = Math.floor(m / 2);
    }

    return result.reverse().join("");
  }

  while (s !== "1") {
    s = removeZero(s);
    s = toBinary(s.length);

    count += 1;
  }

  removeZero(s);

  return [count, zero];
}

console.log(solution("01110"));
