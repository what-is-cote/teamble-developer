const dx = [-1,1,0,0];
const dy = [0,0,-1,1];
function solution(maps) {
    let visit = new Array(maps.length);
    let q = [];
    const n = maps.length;
    const m = maps[0].length;
    
    for(let i=0;i<maps.length;i++){
        visit[i] = new Array(maps[0].length);
    }
    
    for(let i=0;i<n;i++){
        for(let j=0;j<m;j++){
            visit[i][j] = 0;
        }
    }
    
    q.push([0,0]);
    visit[0][0] = 1;
    
    while(q.length){
        for(let i=0;i<q.length;i++){
            let [x,y] = q.shift();
            
            for(let j=0;j<4;j++){
                let nx = x+dx[j];
                let ny = y+dy[j];
                
                if(nx>=0&&nx<n&&ny>=0&&ny<m&&!visit[nx][ny] && maps[nx][ny]){
                    if(nx === n-1 && ny === m-1){
                        return visit[x][y] + 1;
                    }
                    q.push([nx,ny]);
                    visit[nx][ny] = visit[x][y] + 1;
                }
            }
        }
    }
    return -1;
}
