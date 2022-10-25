
function solution(genres, plays) {
    var answer = [];
    let genreObj = {};
    
    function sort(arr){
        arr = arr.sort((a,b)=>{
            if(a[1] > b[1])return -1;
            return 1;
        });
        return arr;
    }
    
    genres.forEach((genre,idx) => {
        if(genreObj[genre] === undefined)genreObj[genre] = 0;
        genreObj[genre] += plays[idx];
    })
    genreObj = sort(Object.entries(genreObj));
    genreObj.forEach(el => {
        let list = [];
        
        for(let i=0;i<genres.length;i++){
            if(genres[i] === el[0]){
                list.push([i,plays[i]]);
            }
        }
        list = sort(list).slice(0,2);
        list.forEach(el => answer.push(el[0]));
    })
    return answer;
}
