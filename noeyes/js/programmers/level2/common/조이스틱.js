function solution(NAME) {
  let [count] = [0];
  let check = [0, 0];
  const name = NAME.split("");
  const lookup = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".split("");

  for (let i = 0; i < name.length; i++) {
    const idx = lookup.indexOf(name[i]);
    if (idx <= 13) count += idx;
    else count += 26 - idx;
    name[i] = "A";

    check[0] = i + 1;
    while (check[0] !== i) {
      if (check[0] >= name.length) check[0] -= name.length;
      if (name[check[0]] !== "A") break;
      check[0] += 1;
      if (check[0] >= name.length) check[0] -= name.length;
    }

    if (check[0] === i) return count;

    check[1] = i - 1;
    while (check[1] !== i) {
      if (check[1] < 0) check[1] += name.length;
      if (name[check[1]] !== "A") break;
      check[1] -= 1;
      if (check[1] < 0) check[1] += name.length;
    }

    if (check[1] === i) return count;

    const next = [...check];
    check[0] > i
      ? (check[0] = check[0] - i)
      : (check[0] = check[0] - i + name.length);
    check[1] > i
      ? (check[1] = i - check[1] + name.length)
      : (check[1] = i - check[1]);

    const min = Math.min(...check);
    min === check[0] ? (i = next[0] - 1) : (i = next[1] - 1);

    count += min;
    check = [0, 0];
  }

  return count;
}

function solution(name) {
  let alpha = name.split("");

  const change = alpha.reduce((a, b) => {
    const num = b.charCodeAt() - 65;
    return (a += num > 13 ? 26 - num : num);
  }, 0);

  let move = alpha.length;
  let N = alpha.length;

  for (let times = 0; times < 2; times++) {
    for (let i = 0; i < N; i++) {
      let j = i + 1;
      while (j != i && alpha[j] == "A") j = (j + 1) % N;
      move = Math.min(move, i + ((N + i - j) % N));
    }

    const tmp = alpha[0];
    alpha = alpha.slice(1).reverse();
    alpha.unshift(tmp);
  }

  return change + move;
}
console.log(solution("ABABAAAAAAABA"));
