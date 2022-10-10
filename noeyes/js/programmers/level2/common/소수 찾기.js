function solution(numbers) {
  const numArr = numbers.split("");
  const set = new Set();
  let count = 0;
  function isPrime(n) {
    if (n <= 1) return false;
    if (n === 2) return true;

    for (let i = 2; i <= Math.sqrt(n, 2); i++) {
      if (n % i === 0) return false;
    }

    return true;
  }

  numArr.forEach((n, i, origin) => {
    tree(n, [...origin.slice(0, i), ...origin.slice(i + 1)]);
  });

  function tree(n, arr) {
    set.add(n - 0);

    arr.forEach((e, i, origin) =>
      tree(n + e, [...origin.slice(0, i), ...origin.slice(i + 1)])
    );
  }

  for (let n of set) isPrime(n) && count++;
  return count;
}

console.log(solution("121"));
