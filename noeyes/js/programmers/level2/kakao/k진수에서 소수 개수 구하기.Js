function solution(n, k) {
  const arr = (n.toString(k) + "").split("");
  let count = 0;
  let [s, e] = [0, 0];
  let str = "";

  function isPrime(subNumber) {
    if (subNumber <= 1) return false;

    for (let i = 2; i <= Math.sqrt(subNumber, 2); i++) {
      if (subNumber % i === 0) return false;
    }

    return true;
  }

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === "0") {
      if (isPrime(str - 0)) count++;
      s = i + 1;
      e = i + 1;
      str = "";
    } else {
      str += arr[i];
      e = i;
    }
  }

  if (
    str &&
    isPrime(str - 0) &&
    (str.length === arr.length || arr[s - 1] === "0")
  )
    count++;
  return count;
}

console.log(solution(100303001, 10));
