const N = 4;
const M = 2;
const result = Array(M);
function DFS(L, S) {
  if (L === M) {
    console.log(result);
    return;
  }

  result[L] = S;

  for (let i = S + 1; i <= N; i++) {
    DFS(L + 1, i);
  }
}

for (let i = 1; i <= N; i++) {
  DFS(0, i);
}
