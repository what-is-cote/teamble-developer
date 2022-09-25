function solution(n, words) {
  const prev = [];

  for (let i = 0; i < words.length; i++) {
    if (i === 0) {
      prev.push(words[i]);
      continue;
    }

    if (words[i][0] !== words[i - 1][words[i - 1].length - 1]) {
      return [(i % n) + 1, Math.floor(i / n) + 1];
    }

    if (prev.includes(words[i])) {
      return [(i % n) + 1, Math.floor(i / n) + 1];
    }

    prev.push(words[i]);
  }

  return [0, 0];
}

// console.log(
//   solution(2, ["hello", "one", "even", "never", "now", "world", "draw"])
// );

["hello", "one", "even", "never", "now", "world", "draw"].reduce(
  (prev, now, idx) => {
    console.log(prev, now, idx);
    return now[now.length - 1];
  }
);
