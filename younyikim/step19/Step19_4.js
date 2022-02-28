const [n, ...input];

for(let i = 0; i < n; i ++) {
    let cnt = 1;
    let M = Number(input[i * 2].split(''[1]));
    const queue = input[i * 2 + 1].split('').map(i => Number(i));

    while(1) {
        const shiftItem = queue.shift();

        // 현재 뺀 값이 목표하는 값이고, 큐 안에 우선순위가 큰 값이 없는 경우(정답인 경우)
        if(Math.max(...queue) <= shiftItem && M === 0) {
            console.log(count);
            break;
        }
        // 현재 뺀 값이 목표하는 값이지만, 큐안에 우선순위가 큰 값이 있을 때
        else if(Math.max(...queue) > shiftItem && M === 0) {
            queue.push(shiftItem);
            M = queue.length - 1;
        }
        // 현재 뺀 값이 목표하는 값이 아니고, 큐안에 우선순위가 큰 값이 있을 때
        else if(Math.max(...queue) > shiftItem) {
            queue.push(shiftItem);
            M -= 1;
        }
        // 현재 뺀 값이 목표하는 값이지만, 큐안에 우선순위가 큰 값이 있을 때
        else if(Math.max(...queue)<= shiftItem) {
            count += 1;
            M -= 1;
        }
    }
}

console.log(n)