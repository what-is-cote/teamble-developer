function solution(n) {
  var ans = 0;

  function r(n) {
    if (n === 0) return;
    if (n % 2 === 1) {
      ans += 1;
      r(n - 1);
    } else r(n / 2);
  }

  r(n);
  return ans;
}

console.log(solution(5000));
