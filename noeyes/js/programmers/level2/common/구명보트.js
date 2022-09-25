function solution(people, limit) {
  var answer = 0;
  let l = 0;
  let r = people.length - 1;
  people.sort((v1, v2) => v2 - v1);

  while (l <= r) {
    if (l === r) {
      answer += 1;
      return answer;
    } else if (people[l] + people[r] <= limit) {
      l++;
      r--;
      answer += 1;
    } else {
      l++;
      answer += 1;
    }
  }

  return answer;
}

console.log(solution([70, 50, 80, 60, 40, 40, 40], 100));

// 80 70 60 50 40 40 40  5
