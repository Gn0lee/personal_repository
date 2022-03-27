function solution(s) {
    var answer = s.length;
    
    function cutString(s , n){
        var sList = [... s];
        var returnList = [];
        var tmp = '';
        
        for(var i = 1; i <= s.length; i++){
            tmp += sList[i-1];
            if(i % n === 0){
                returnList.push(tmp);
                tmp = '';
            }
        }
        if(tmp.length !==0){
            returnList.push(tmp);
        }
        return returnList;
    }
    
    for(var i = 1 ; i <= parseInt(s.length/2) ; i++){
        var cuted = cutString(s,i);
        var compressed = [];
        while(cuted.length){
            var curr = cuted.shift();
            var tmp = 1;
            
            while(curr === cuted[0] && cuted.length){
                tmp += 1;
                cuted.shift();
            }
            
            if(tmp > 1){
                compressed.push(tmp+curr);
            }else{
                compressed.push(curr);
            }
        }
        // console.log(compressed)
        answer = Math.min(answer , compressed.join("").length);
    }
    
    
    return answer;
}

console.log(solution("aabbaccc"));