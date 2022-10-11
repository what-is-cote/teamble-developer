function solution(k, dungeons) {
  function enterTheDungeons(D) {
    const info = [];
    if (D.length === 1) {
      const f = D[0][0] <= k ? k - D[0][1] : k;
      return [
        {
          f,
          count: 1,
        },
      ];
    }

    D.forEach((d, i, origin) => {
      const avail = enterTheDungeons([...D.slice(0, i), ...D.slice(i + 1)]);
      avail.forEach((each) => {
        if (d[0] <= each.f) {
          info.push({
            f: each.f - d[1],
            count: each.count + 1,
          });
        } else {
          info.push(each);
        }
      });
    });

    return info;
  }

  return Math.max(...enterTheDungeons(dungeons, k).map((e) => e.count));
}

console.log(
  solution(80, [
    [80, 20],
    [50, 40],
    [30, 10],
  ])
);
