function solution(record) {
  const lookup = {};
  const answer = [];
  record
    .map((e) => {
      const r = e.split(" ");

      if (r[0] === "Enter") {
        lookup[r[1]] = r[2];
      } else if (r[0] === "Change") {
        lookup[r[1]] = r[2];
      }
      return r;
    })
    .forEach((r) => {
      if (r[0] === "Enter") {
        answer.push(`${lookup[r[1]]}님이 들어왔습니다.`);
      } else if (r[0] === "Leave") {
        answer.push(`${lookup[r[1]]}님이 나갔습니다.`);
      }
    });

  return answer;
}

console.log(
  solution([
    "Enter uid1234 Muzi",
    "Enter uid4567 Prodo",
    "Leave uid1234",
    "Enter uid1234 Prodo",
    "Change uid4567 Ryan",
  ])
);
