function solution(queue1, queue2) {
  const origin1 = [...queue1];
  const origin2 = [...queue2];
  let [sum1, sum2, count, p1, p2] = Array(5).fill(0);

  for (let i = 0; i < queue1.length; i++) {
    sum1 += queue1[i];
    sum2 += queue2[i];
  }

  if ((sum1 + sum2) % 2 === 1) return -1;

  while (sum1 !== sum2) {
    if (sum1 < sum2) {
      const v = queue2[p2++];
      queue1.push(v);
      sum2 -= v;
      sum1 += v;
    } else {
      const v = queue1[p1++];
      queue2.push(v);
      sum1 -= v;
      sum2 += v;
    }

    count += 1;
    if (count > (origin1.length + origin2.length) * 2) return -1;
  }

  return count;
}

console.log(solution([1, 2], [3, 2]));
