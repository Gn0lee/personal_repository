function solution(gems) {
    var answer = [1,gems.length];
    var totalGems = new Set(gems);
    var totalSize = totalGems.size;
    var gemMap = new Map();
    var start = 0;
    var end = 1;
    
    gemMap.set(gems[0], 1);
    
    while(end <= gems.length){
        if(gemMap.size === totalSize){
            // console.log(start,end,"1")
            if(end-1-start < answer[1] - answer[0]){
                // console.log(start, end)
                answer[1] = end;
                answer[0] = start + 1;
            }
            
            var tmp = gemMap.get(gems[start]);
            
            if(tmp === 1){
                gemMap.delete(gems[start]);
            }else{
                gemMap.set(gems[start], tmp -1);
            }
            
            start += 1;
        }else{
            var tmp1 = gemMap.get(gems[end]);
            tmp1 ? gemMap.set(gems[end], tmp1+1) : gemMap.set(gems[end], 1);
            end += 1;
        }
    }
    

    return answer;
}