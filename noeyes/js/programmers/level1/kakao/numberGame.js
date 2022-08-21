function solution(s) {
  const numbers = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
  ];

  let i = 0;
  let answer = "";

  while (i < s.length) {
    if (Number.isInteger(s[i] - 0)) {
      answer += s[i++];
    } else {
      let word = "";

      while (!Number.isInteger(s[i] - 0) && i < s.length) {
        word += s[i++];

        if (numbers.indexOf(word) !== -1) {
          answer += numbers.indexOf(word);
          word = "";
        }
      }
    }
  }

  return answer - 0;
}

console.log(solution("2three45sixseven"));
