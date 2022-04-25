function solution(board) {
    var n = board.length;
    var answer = 1000000000;
    function BFS(start){
        var q = [start];
        
        var dy = [1,0,-1,0], dx = [0,1,0,-1];
        var visited = Array.from({length : n}, () => 0).map((elem) => Array.from({length : n}, () => 0));
        
        while(q.length > 0){
            var [nowY , nowX , dir , cost] = q.shift();
            
            if(nowY === n-1 && nowX === n-1){
                answer = Math.min(answer, cost);
            }
            
            for(var i = 0 ; i < 4 ; i++){
                var nextY = nowY + dy[i], nextX = nowX + dx[i];
                if(nextY < 0 || nextY >= n || nextX < 0 || nextX >= n || board[nextY][nextX] === 1){
                    continue;
                }
                var nextCost = (dir === i) ? cost + 100 : cost + 600;
                
                if(visited[nextY][nextX] === 0 || visited[nextY][nextX] >= nextCost){
                    q.push([nextY, nextX, i , nextCost]);
                    visited[nextY][nextX] = nextCost;
                }                
            }
        }
        return answer;
    }
    
    
    var answer1 = BFS([0,0,0,0]), answer2 = BFS([0,0,1,0]);
    
    
    return Math.min(answer1,answer2);
}