function solution(s) {
  function r(str) {
    let temp = "";

    for (let i = 0; i < str.length; i++) {
      if (str[i] === str[i + 1]) {
        temp = temp + (str.slice(0, i) + str.slice(i + 2));
        break;
      } else {
        temp += str[i];
      }
    }

    if (!temp) return 1;
    else if (temp === str) return 0;
    else return r(temp);
  }