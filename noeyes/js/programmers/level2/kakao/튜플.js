function solution(s) {
  const lookup = {};
  let num = "";

  for (let i = 0; i < s.length; i++) {
    if (Number.isInteger(s[i] - 0)) {
      num += s[i];
    } else if (num) {
      lookup[num] = lookup[num] === undefined ? 1 : lookup[num] + 1;
      num = "";
    }
  }
  const keys = Object.keys(lookup);
  const answer = Array(keys.length);

  for (let k of keys) {
    answer[Math.abs(lookup[k] - keys.length)] = k - 0;
  }

  return answer;
}

/**
 * 길이 순으로 정렬 후
 * 앞 원소와 곂치지 않는 원소를 찾는 것도 방법
 */
