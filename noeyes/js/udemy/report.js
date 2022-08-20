function solution(id_list, report, k) {
  var answer = Array(id_list.length).fill(0);

  const reportCount = {};
  const userList = {};

  report.forEach((e) => {
    const reportedInfo = e.split(" ");
    const user = reportedInfo[0];
    const bad = reportedInfo[1];

    if ((userList[bad] && !userList[bad].includes(user)) || !userList[bad]) {
      reportCount[bad] = reportCount[bad] ? reportCount[bad] + 1 : 1;
      userList[bad] ? userList[bad].push(user) : (userList[bad] = [user]);
    }
  });
  console.log(userList);
  for (let name of id_list) {
    if (userList[name] && reportCount[name] >= k) {
      userList[name].forEach((user) => {
        answer[id_list.indexOf(user)] += 1;
      });
    }
  }

  return answer;
}

console.log(
  solution(
    ["muzi", "frodo", "apeach", "neo"],
    ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
    2
  )
);
