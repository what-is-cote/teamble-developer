function solution(want, number, discount) {
    var answer = 0;
    let len = discount.length - 9;
    for(let i=0;i<len;i++){
        const arr = discount.slice(i,10+i);
        const num = [...number];
        for(let j=0;j<want.length;j++){
            if(arr.includes(want[j])){
                let count = arr.filter((el)=>el === want[j]).length;
                num[j] -= count;
                arr.filter((el)=>el === want[j]);
            }
        }
        if(num.every((n)=>n <= 0)){
            answer++;
        }
    }
    return answer;
}
