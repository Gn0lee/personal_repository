function solution(maps) {
    var answer = 0;
    var n = maps.length;
    var m = maps[0].length;
    var dy = [-1,0,1,0];
    var dx = [0,1,0,-1];
    var q = [[0,0]];
    
    while(q.length > 0){
        var [nowY,nowX] = q.shift();
        
        for(var i = 0 ; i < 4 ; i++){
            var nextY = nowY + dy[i];
            var nextX = nowX + dx[i];
            if(0<= nextY && nextY < n && 0<= nextX && nextX < m && maps[nextY][nextX] === 1){
                q.push([nextY,nextX]);
                maps[nextY][nextX] = maps[nowY][nowX] + 1;
            }
        }
    }
    
    if(maps[n-1][m-1] === 1){
        answer = -1;
    }else{
        answer =maps[n-1][m-1];
    }
    
    return answer;
}