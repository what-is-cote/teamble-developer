// Multiple Pointers - isSubsequence
// Write a function called isSubsequence which takes in two strings
// and checks whether the characters in the first string form a subsequence of
// the characters in the second string.
// In other words, the function should check whether the characters in the first string
// appear somewhere in the second string, without their order changing.

// Your solution MUST have AT LEAST the following complexities:

// Time Complexity - O(N + M)

// Space Complexity - O(1)

// O(N * M) 인 듯..
// function isSubsequence(str1, str2) {
//   if (str2.length < str1.length) return false;

//   let p1 = 0;

//   while (p1 < str1.length) {
//     if (str2.indexOf(str1[p1]) === -1) return false;
//     else {
//       str2 = str2.slice(str2.indexOf(str1[p1]) + 1);
//     }
//     console.log(str2);
//     p1 += 1;
//   }

//   return true;
// }

function isSubsequence(str1, str2) {
  if (str2.length < str1.length) return false;

  let p1 = 0;
  let p2 = 0;

  while (p2 < str2.length) {
    if (str1[p1] === str2[p2]) {
      p1 += 1;
      p2 += 1;
    } else {
      p2 += 1;
    }

    if (p1 === str1.length) return true;
  }

  return false;
}

console.log(isSubsequence("acb", "ackdoensb"));
