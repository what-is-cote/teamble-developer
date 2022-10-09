function gcd(a,b){
    let c;
    while(b > 0){
        c = a % b;
        a = b;
        b = c;
    }
    return a;
}
function lcm(a,b){
    return a * b / gcd(a,b);
}
function solution(arr) {
    const answer = arr.reduce((a,b)=>{
        a = lcm(a,b);
        return a;
    });
    return answer;
}
