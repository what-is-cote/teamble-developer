function solution(numbers) {
    let answer = [];
    numbers.forEach((number) => {
        let diff = -1;
        let p = 0;
        let a = number.toString(2);
        let tmp = '';
        let cnt = 0;
        while(diff > 2 || diff < 0){
            diff = 0;
            const next = number + Math.pow(2,p++);
            tmp = next;
           let b = next.toString(2);
            a = a.padStart((a.length > b.length ? a.length : b.length), '0');
            b = b.padStart((a.length > b.length ? a.length : b.length), '0');
            for(let i=0;i<a.length;i++){
                if(a[i] !== b[i])diff++;
            }
        }
        answer.push(tmp);
    });
    return answer;
}
