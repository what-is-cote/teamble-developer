/**
 * Write a function called sameFrequency. Given two positive integers, find out if the two numbers have the same frequency of digits.
 * Your solution MUST have the following complexities:
 * Time: O(N)
 */

function sameFrequency(num1, num2) {
  let str1 = num1 + "";
  let str2 = num2 + "";

  if (str1.length !== str2.length) return false;

  let lookup = {};

  for (let char of str1) {
    lookup[char] ? (lookup[char] += 1) : (lookup[char] = 1);
  }

  for (let char of str2) {
    //개수가 0이거나 존재하지 않는 숫자여서 undefined인 경우
    if (!lookup[char]) return false;
    else {
      lookup[char] -= 1;
    }
  }

  return true;
}

console.log(sameFrequency(222, 22));
