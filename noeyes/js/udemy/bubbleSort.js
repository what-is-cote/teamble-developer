/**
 * 일반적인 경우엔 O(n2)
 * 최적화 + 거의 정렬된 경우엔 O(n)까지 가능
 * 정렬된 데이터일수록 유리하다
 */

function bubbleSort(arr) {
  let limit = arr.length;

  //최적화
  let noSwap;
  while (limit > 1) {
    noSwap = true;
    for (let j = 0; j < limit - 1; j++) {
      if (arr[j] > arr[j + 1]) {
        [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
        noSwap = false;
      }
    }
    if (noSwap) break;
    limit--;
  }

  return arr;
}

console.log(bubbleSort([2, 1, 3, 4, 5, 6, 7, 8, 9, 10]));
