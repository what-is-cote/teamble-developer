function solution(files) {
    const answer = files.sort((a,b)=>{
        let [matchA, matchB] = [a.match(/[0-9]+/), b.match(/[0-9]+/)];
        let [headA, headB] = [a.slice(0, matchA.index).toLowerCase(), b.slice(0, matchB.index).toLowerCase()];
        let [numA, numB] = [+matchA[0], +matchB[0]];
        if(headA === headB){
            if(numA > numB)return 1;
            if(numA < numB)return -1;
            else return 0;
        }else{
            if(headA > headB)return 1;
            else return -1;
        }
    })
    return answer;
}
