function solution(s) {
  const arr = s
    .split(" ")
    .map((e) => e - 0)
    .sort((a, b) => a - b);

  return `${arr[0]} ${arr.pop()}`;
}

console.log(solution("-11 -12"));
