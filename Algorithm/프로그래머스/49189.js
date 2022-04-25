function solution(n, edge) {
    var answer = 1;
    const graph = new Map();
    const visited = {};
    var answerList = {};
    
    for(var i = 1 ; i <=n ; i++){
        graph[i] = [];
        visited[i] = false;
    };
    
    edge.forEach(([start, end]) => {
        graph[start].push(end);
        graph[end].push(start);
    });
    // console.log(graph);
    var q = [1];
    visited[1] = true;
    var level = 0;
    
    while(q.length > 0){
        const length = q.length;
        for(var i = 0 ; i < length ; i ++){
            var now = q.shift();
            console.log("now : ", now);
            if(answerList[level] === undefined){
                console.log("처음 갱신,now : ",now, "level : ",level);
                answerList[level] = 1;
            }else{
                console.log("추가 갱신,now : ",now, "level : ",level);
                answerList[level] += 1;    
            }
            graph[now].forEach((next) => {
                if(visited[next] === false){
                    visited[next] = true;
                    q.push(next);
                }
            });
            console.log("for문 종료");
        }
        level += 1;
    }
    
    console.log(answerList, visited);
    answer = answerList[level];
    
    return answer;
}

solution(6	,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]);