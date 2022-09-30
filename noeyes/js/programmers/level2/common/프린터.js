function solution(priorities, location) {
  let max = Math.max(...priorities);
  let myPriority = priorities[location];
  let len = priorities.length;
  let pt = 0;
  let origin = pt;
  let count = 1;

  while (myPriority !== max || origin !== location) {
    if (priorities[pt] === max) {
      priorities.push(-1);
      count += 1;
    } else {
      priorities.push(priorities[pt]);
    }

    pt += 1;
    origin = pt;

    while (origin >= len) {
      origin -= len;
    }

    max = Math.max(...priorities.slice(pt));
  }

  return count;
}

console.log(solution([1, 1, 9, 1, 1, 1], 5));
