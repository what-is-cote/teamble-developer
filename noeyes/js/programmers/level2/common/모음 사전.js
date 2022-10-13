function solution(word) {
  var answer = 0;
  const vowel = ["A", "E", "I", "O", "U"];
  const search = [];

  while (true) {
    if (search.join("") === word) return answer;

    if (search.length < 5) {
      search.push("A");
    } else {
      if (search[search.length - 1] === "U")
        while (search[search.length - 1] === "U") search.pop();

      search[search.length - 1] =
        vowel[vowel.indexOf((last = search[search.length - 1])) + 1];
    }

    answer += 1;
  }
}

console.log(solution("EIO"));
