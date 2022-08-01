// Frequency Counter / Multiple Pointers - areThereDuplicates
// Implement a function called, areThereDuplicates which accepts a variable number of arguments, and checks whether there are any duplicates among the arguments passed in.
// You can solve this using the frequency counter pattern OR the multiple pointers pattern.

//  Restrictions:
//  Time - O(n)
//  Space - O(n)
//  Bonus:
//  Time - O(n log n)
//  Space - O(1)

function areThereDuplicates(...args) {
  if (args.length <= 1) return false;

  let lookup = {};

  for (let char of args) {
    if (lookup[char]) return true;
    else {
      lookup[char] = true;
    }
  }

  return false;

  return new Set(arguments).size !== arguments.length;
}

console.log(areThereDuplicates(1, 2, 3));
