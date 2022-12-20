function solution(n, wires) {
    let answer = 987654321;
    let visit = Array(n+1).fill(false);
    
    function dfs(cur,info){
        visit[cur] = true;
        for(let next of info[cur]){
            if(!visit[next]){
                dfs(next,info);
            }
        }
    }
    
    for(let i=0;i<wires.length;i++){
        const tmp = [...wires.slice(0,i),...wires.slice(i+1)];
        const info = {};
        visit = Array(n+1).fill(false);
        
        for(let i=1;i<=n;i++){
            info[i] = [];
        }
        
        tmp.forEach(wire => {
            const [a,b] = wire;
            info[a] = [...info[a],b];
            info[b] = [...info[b],a];
        });
        dfs(1,info);
        const a = visit.filter(x => x).length;
        const b = n - a;
        answer = Math.min(answer, Math.abs(a-b));
    }
    return answer;
}
