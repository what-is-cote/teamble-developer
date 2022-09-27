function solution(clothes) {
  let answer = 1;
  const lookup = {};

  for (let [cloth, category] of clothes) {
    lookup[category] =
      lookup[category] === undefined ? 1 : lookup[category] + 1;
  }

  for (let category in lookup) {
    answer *= 1 + lookup[category];
  }

  return answer - 1;
}

console.log(
  solution([
    ["yellow_hat", "headgear"],
    ["blue_sunglasses", "eyewear"],
    ["green_turban", "headgear"],
  ])
);
