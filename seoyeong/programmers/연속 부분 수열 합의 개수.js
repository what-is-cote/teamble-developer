function solution(elements) {
    const set = new Set(elements);
    for(let i=2;i<=elements.length;i++){
        for(let j=0;j<elements.length;j++){
            let arr = elements.slice(j,j+i);
            if(arr.length !== i){
                arr = [...arr, ...elements.slice(0,i-arr.length)];
            }
            set.add([...arr].reduce((a,b)=> (+a) + (+b), 0));
        }
    }
    return set.size;
}
