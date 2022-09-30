function solution(fees, records) {
  const IN = {};
  const TIME = {};

  function cumulate(in_time, out_time) {
    const inTime = in_time.split(":");
    const outTime = out_time.split(":");
    const m =
      outTime[1] - inTime[1] < 0
        ? outTime[1] - inTime[1] + 60
        : outTime[1] - inTime[1];
    const h =
      outTime[1] - inTime[1] < 0
        ? outTime[0] - inTime[0] - 1
        : outTime[0] - inTime[0];
    const time = h * 60 + m;

    return time;
  }

  records
    .map((r) => r.split(" "))
    .forEach((r) => {
      if (r[2] === "IN") IN[r[1]] = r[0];
      else {
        const time = cumulate(IN[r[1]], r[0]);
        delete IN[r[1]];
        TIME[r[1]] = TIME[r[1]] ? TIME[r[1]] + time : time;
      }
    });

  for (let n in IN) {
    const time = cumulate(IN[n], "23:59");
    delete IN[n];
    TIME[n] = TIME[n] ? TIME[n] + time : time;
  }

  const arr = [];
  for (let number in TIME) {
    arr.push([
      number,
      TIME[number] <= fees[0]
        ? fees[1]
        : fees[1] + Math.ceil((TIME[number] - fees[0]) / fees[2]) * fees[3],
    ]);
  }

  return arr.sort((p, c) => p[0] - c[0]).map((e) => e[1]);
}
console.log(
  solution(
    [120, 0, 60, 591],
    [
      "16:00 3961 IN",
      "16:00 0202 IN",
      "18:00 3961 OUT",
      "18:00 0202 OUT",
      "23:58 3961 IN",
    ]
  )
);
