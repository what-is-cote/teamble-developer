function solution(s) {
  const stack = [];

  for (let i = 0; i < s.length; i++) {
    if (s[i] === "(") stack.push(s[i]);
    else if (stack.pop() !== "(") return false;
  }

  return stack.length === 0;
}

console.log(solution("())"));
