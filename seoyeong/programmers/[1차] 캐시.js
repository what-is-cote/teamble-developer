function solution(cacheSize, cities) {
    let answer = 0;
    cities = cities.map((city)=>city.toLowerCase());
    let arr = []; 
    for(let i=0;i<cities.length;i++){
        let cur = cities[i];
        
        if(arr.includes(cur)){ // hit
            arr = arr.filter((city)=>city !== cur);
            arr.push(cur);
            answer += 1;
        }else{ // miss
            arr.push(cur);
            if(arr.length > cacheSize){
                arr.shift();
            }
            answer += 5;
        }
    }
    return answer;
}
