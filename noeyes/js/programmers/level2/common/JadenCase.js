function solution(s) {
  var answer = "";
  let flag = 1;
  function isNumber(c) {
    return Number.isInteger(c - 0);
  }
  for (let i = 0; i < s.length; i++) {
    if (s[i] === " ") {
      answer += s[i];
      flag = 1;
      continue;
    }

    if (isNumber(s[i])) {
      answer += s[i];
    } else {
      if (flag) {
        answer += s[i].toUpperCase();
      } else {
        answer += s[i].toLowerCase();
      }
    }

    flag = 0;
  }

  return answer;
}

console.log(solution("3people unFollowed me"));
