let N, M, result = 0;
let dq = [];
let find = []; // 입력받은 input 값

for(let i = 1; i <= N; i++) {
    dq.push(i);
}

for(let i = 0; i < M; i++) {
    let idx = dq.indexOf();
    let mid;

    // if queue size is even
    if(dq.length() % 2) {
        mid = dq.length() / 2 - 1;
    } else { // if queue is odd
        mid = dq.length() / 2;
    }

    // case 2: rotate left
    if(idx <= mid){
        for(let j = 0; j < idx; j++) {
            let tmp = dq.shift();
            dq.push(tmp);
            result ++
        }
    }
    // case 3 : rotate right
    else {
        for (let j = 0; j < dq.length() - idx; j++) {
            let tmp = dq.pop();
            dq.unshift(tmp);
            result++;
        }
    }
    dq.shift();
}

console.log(result)