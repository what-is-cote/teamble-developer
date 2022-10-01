function solution(msg) {
  let dic = "0ABCDEFGHIJKLMNOPQRSTUVWXYZ".split("");
  let answer = [];

  for (let i = 0; i < msg.length; i++) {
    let subStr = msg[i];

    for (let j = i + 1; j <= msg.length; j++) {
      if (dic.includes(subStr + msg[j])) {
        subStr += msg[j];
        i = j;
      } else {
        answer.push(dic.indexOf(subStr));
        dic.push(subStr + msg[j]);
        break;
      }
    }
  }
  return answer;
}

console.log(solution("ABABABABABABABAB"));
