const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const n = parseInt(input.shift());
let cnt = 0;
let cur = 666;
let answer = "";
while (cnt !== n) {
  let next = cur.toString();
  if (next.match(/666+/)) {
    cnt++;
    answer = next;
  }
  cur++;
}
console.log(answer);
