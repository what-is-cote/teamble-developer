function solution(cacheSize, cities) {
  let answer = 0;

  if (!cacheSize) return cities.length * 5;

  cities.reduce((prev, cnt, idx) => {
    cnt = cnt.toLowerCase();
    if (!prev) {
      answer += 5;

      return [cnt];
    }
    if (prev.includes(cnt)) {
      answer += 1;

      const idx = prev.indexOf(cnt);
      prev = prev
        .slice(0, idx)
        .concat(prev.slice(idx + 1))
        .concat([cnt]);

      return prev;
    } else {
      answer += 5;

      if (prev.length < cacheSize) {
        prev.push(cnt);
      } else {
        prev = prev.splice(1);
        prev.push(cnt);
      }

      return prev;
    }
  }, null);

  return answer;
}

console.log(
  solution(3, [
    "Jeju",
    "Pangyo",
    "Seoul",
    "Jeju",
    "Pangyo",
    "Seoul",
    "Jeju",
    "Pangyo",
    "Seoul",
  ])
);
