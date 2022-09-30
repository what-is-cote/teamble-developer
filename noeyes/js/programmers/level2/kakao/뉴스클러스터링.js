function solution(str1, str2) {
  const S1 = {};
  const S2 = {};
  let intersection = 0;
  let union = 0;
  str1 = str1.toLowerCase();
  str2 = str2.toLowerCase();

  for (let i = 0; i < str1.length - 1; i++) {
    if (str1[i].toLowerCase() === str1[i].toUpperCase()) continue;
    if (str1[i + 1].toLowerCase() === str1[i + 1].toUpperCase()) continue;
    S1[str1[i] + str1[i + 1]]
      ? (S1[str1[i] + str1[i + 1]] += 1)
      : (S1[str1[i] + str1[i + 1]] = 1);
  }

  for (let i = 0; i < str2.length - 1; i++) {
    if (str2[i].toLowerCase() === str2[i].toUpperCase()) continue;
    if (str2[i + 1].toLowerCase() === str2[i + 1].toUpperCase()) continue;
    S2[str2[i] + str2[i + 1]]
      ? (S2[str2[i] + str2[i + 1]] += 1)
      : (S2[str2[i] + str2[i + 1]] = 1);
  }
  if (!Object.keys(S1).length && !Object.keys(S2).length) return 65536;

  for (let s in S1) {
    if (s in S2) {
      if (S2[s] >= S1[s]) {
        intersection += S1[s];
        S2[s] -= S1[s];
      } else {
        intersection += S2[s];
        delete S2[s];
      }
    }
    union += S1[s];
  }
  Object.entries(S2).forEach(([k, v]) => (union += v));

  return Math.floor((intersection / union) * 65536);
}

console.log(solution("E=M*C^2", "e=m*c^2"));
