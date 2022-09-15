function solution(info, edges) {
    let answer = 0;
    const graph = Array.from({length:info.length}, () => [])
    
    for(const [parent,child] of edges){
        graph[parent].push(child)
    }
    
    function dfs(currNode, sheep, wolf, next){
        info[currNode] ? wolf++ : sheep++;
        
        if(sheep === wolf) return;
        
        next.push(...graph[currNode])
        next.forEach((el,idx,arr) => {
            const exceptCurr = arr.filter((item,i) => i !== idx)
            
            dfs(el,sheep, wolf, exceptCurr)
        })
        
        answer = Math.max(answer, sheep)
        return;
    }
    
    dfs(0,0,0,[])
    
    return answer;
}