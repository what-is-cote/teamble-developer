function solution(s) {
  const stack = [];
  let pt = -1;
  if (s.length % 2 !== 0) return 0;
  for (let i = 0; i < s.length; i++) {
    if (stack[pt] === s[i]) {
      stack.pop();
      pt--;
    } else {
      stack.push(s[i]);
      pt++;
    }
  }

  return stack.length ? 0 : 1;
}

console.log(solution("ccddcd"));
