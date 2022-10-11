function checkNumber(map,str){
    for(let i=0;i<str.length;i++){
        if(map[str[i]] > 0)map[str[i]]++;
        else map[str[i]] = 1;
    }
}
function solution(X, Y) {
    var answer = '';
    const x = {};
    const y = {};
    checkNumber(x,X);
    checkNumber(y,Y);
    
    const tmp = {};
    if(Object.keys(x).length < Object.keys(y).length){
        for(let key in x){
            if(y[key] > 0){
                tmp[key] = x[key] > y[key] ? y[key] : x[key];
            }
        }
    }else{
        for(let key in y){
            if(x[key] > 0){
                tmp[key] = x[key] > y[key] ? y[key] : x[key];
            }
        }
    }
    if(Object.keys(tmp).length === 0)return "-1";
    else{
        for(let key in tmp){
            answer += key.repeat(tmp[key]);
        }
    }
    answer = answer.split('').reverse().join('');
    if(answer[0] === '0')return '0';
    return answer;
}
