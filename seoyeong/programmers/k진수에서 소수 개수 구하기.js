function isPrime(n) {
    if(n < 2)return 0;
    for(let i=2;i<=Math.sqrt(n);i++){
        if(n % i == 0)return 0;
    }
    return 1;
}
function solution(n, k) {
    let answer = 0;
    let num = n.toString(k);
    let tmp = "0";
    [...num].forEach((n)=>{
        if(n == 0){
            answer += isPrime(tmp);
            tmp = '0';
        }else{
            if(tmp == '0')tmp = "";
            tmp = tmp.concat(n);
        }
    });
    if(tmp){
        answer += isPrime(tmp);
    }
    return answer;
}
