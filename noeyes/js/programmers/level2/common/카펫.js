function solution(brown, yellow) {
  const brownSection = [brown - 2, 2];
  let bW = brownWidth(brownSection[0]);
  let bH = brownHeight(brownSection[1]);

  function brownWidth(n) {
    return n / 2;
  }

  function brownHeight(n) {
    return n / 2 + 2;
  }

  while (bW >= bH) {
    const yellowRow = bW - 2;
    const yellowColumn = bH - 2;

    if (yellow === yellowRow * yellowColumn) {
      return [bW, bH];
    }

    brownSection[0] = brownSection[0] - 2;
    brownSection[1] = brownSection[1] + 2;
    bW = brownWidth(brownSection[0]);
    bH = brownHeight(brownSection[1]);
  }
}

console.log(solution(8, 1));
// 갈색 가로 세로 최소 3
// 갈색 세로 <= 가로
// 노랑 세로 < 갈색 세로

// 아마 노랑의 세로 <= 가로
