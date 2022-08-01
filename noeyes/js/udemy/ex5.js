// Multiple Pointers - averagePair
// Write a function called averagePair.
// Given a sorted array of integers and a target average, determine if there is a pair of values in the array where the average of the pair equals the target average.
// There may be more than one pair that matches the average target.

// Bonus Constraints:
// Time: O(N)
// Space: O(1)

//O(N^2)인 듯
// function averagePair(arr, target) {
//   if (arr.length <= 1) return false;

//   let left = 0;
//   let right = 1;

//   while (left < arr.length && right < arr.length) {
//     if ((arr[left] + arr[right]) / 2 === target) return true;
//     else if ((arr[left] + arr[right]) / 2 > target) {
//       left += 1;
//       right = left + 1;
//     } else {
//       right += 1;

//       if (right === arr.length) {
//         left += 1;
//         right = left + 1;
//       }
//     }
//   }

//   return false;
// }

function averagePair(arr, target) {
  if (arr.length <= 1) return false;

  let left = 0;
  let right = arr.length - 1;
  while (left !== right) {
    if ((arr[left] + arr[right]) / 2 === target) return true;
    else if ((arr[left] + arr[right]) / 2 < target) {
      left += 1;
    } else {
      right -= 1;
    }
  }

  return false;
}

console.log(averagePair([1, 2, 3, 8, 16], 2.5));
