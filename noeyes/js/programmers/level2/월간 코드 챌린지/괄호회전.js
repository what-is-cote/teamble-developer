function solution(s) {
  let stack = [];
  let answer = 0;

  function isOpen(c) {
    switch (c) {
      case "(":
        return true;
      case "{":
        return true;
      case "[":
        return true;
      default:
        false;
    }
  }

  function isPair(s, e) {
    switch (s) {
      case "(":
        if (e === ")") return true;
        else return false;
      case "{":
        if (e === "}") return true;
        else return false;
      case "[":
        if (e === "]") return true;
        else return false;
      default:
        false;
    }
  }

  for (let i = 0; i < s.length; i++) {
    for (var j = 0; j < s.length; j++) {
      if (isOpen(s[j])) {
        stack.push(s[j]);
      } else {
        const c = stack.pop();
        if (!c || !isPair(c, s[j])) break;
      }
    }

    if (j === s.length && stack.length === 0) answer += 1;
    stack = [];
    s = s.slice(1) + s[0];
  }

  return answer;
}

console.log(solution("{{{{{"));
