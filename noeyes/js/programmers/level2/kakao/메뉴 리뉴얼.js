function solution(orders, course) {
  const answer = [];
  const lookup = {};
  // const sort = orders
  //   .map((e) =>
  //     e
  //       .split("")
  //       .join("")
  //   )
  //   .sort((a, b) => a.length - b.length);
  const mutation = orders.map((e) =>
    e.split("").sort((a, b) => {
      if (a < b) return -1;
      if (a > b) return 1;
      if (a === b) return 0;
    })
  );

  const getCombinations = (array, selectNumber) => {
    const results = [];
    if (selectNumber === 1) {
      return array.map((element) => [element]);
    }
    array.forEach((fixed, index, origin) => {
      const rest = origin.slice(index + 1);
      const combinations = getCombinations(rest, selectNumber - 1);
      // console.log(combinations);
      const attached = combinations.map((combination) => {
        const mixed = fixed + combination.join();

        if (mixed.length === selectNumber) {
          lookup[mixed] ? (lookup[mixed] += 1) : (lookup[mixed] = 1);
        }
        return mixed;
      });
      console.log(attached);
      results.push(attached);
    });
    return results;
  };

  mutation.forEach((e) => {
    e.forEach((c, i) => {
      if (i >= 1) {
        getCombinations(e, i + 1);
        // console.log(getCombinations(e, i + 1));
      }
    });
  });
  console.log(lookup);
}

// console.log(
//   solution(["ABCDE", "AB", "CD", "DAE", "XYZ", "XYZ", "ACD"], [2, 3, 4])
// );

const getCombinations = (array, selectNumber) => {
  const results = [];
  if (selectNumber === 1) {
    return array.map((element) => [element]);
  }
  array.forEach((fixed, index, origin) => {
    const rest = origin.slice(index + 1);
    const combinations = getCombinations(rest, selectNumber - 1);
    const attached = combinations.map((combination) => [fixed, ...combination]);
    results.push(...attached);
  });
  return results;
};
console.log(getCombinations([1, 2, 3, 4], 3));
