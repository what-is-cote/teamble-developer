// Write a function called productOfArray which takes in an array of numbers and returns the product of them all.

// productOfArray([1,2,3]) // 6
// productOfArray([1,2,3,10]) // 60

function productOfArray(arr) {
  if (arr.length < 1) return 1;

  let result = arr[0];

  result *= productOfArray(arr.slice(1));

  return result;
}

console.log(productOfArray([1, 2, 3, 10]));
