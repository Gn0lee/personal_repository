function solution(n, k, cmd) {
    var answer = "";
    var pair = {};
    var deleted = [];
    var deletedObj = {};
    
    for(var i = 0; i < n ; i++){
        pair[i] = i;
    }
    // console.log(pair);
    
    for(var currentCmd of cmd){
        switch (currentCmd[0]){
            case "D":
                var [cmd , value] = currentCmd.split(" ");
                k += parseInt(value);
                // console.log("D", k);
            break;
                
            case "C":    
                // console.log("before Delete", k, pair);
                deleted.push([k,pair[k]]);
                deletedObj[pair[k]] = 1;
                var lastIdx = Object.keys(pair).length - 1;
                
                if(k !== lastIdx){
                    for(var j = k ; j < lastIdx ; j++){
                        pair[j] = pair[j+1];
                    }
                    delete pair[lastIdx];
                }else{
                    delete pair[lastIdx];
                    k -= 1;
                }
                // console.log("after Delete", k, pair);
            break;
                
            case "U":
                var [cmd , value] = currentCmd.split(" ");
                k -= parseInt(value);
                // console.log("U", k);
            break;
                
            case "Z":
                // console.log("before undo", k, pair);
                var lastIdx = Object.keys(pair).length - 1;
                var [deletedIdx , deletedValue] = deleted.pop();
                delete deletedObj[deletedValue];
                if(deletedIdx === lastIdx + 1){
                    pair[deletedIdx] = deletedValue;
                    // console.log("after undo", k, pair);
                    break;
                }else{
                    for(var l = lastIdx + 1; l > deletedIdx; l-- ){
                        pair[l] = pair[l-1];
                    }
                    pair[deletedIdx] = deletedValue;
                    if(k >= deletedIdx){
                        k += 1;
                    }
                }
                // console.log("after undo", k, pair);
            break;
        }
    }
    // console.log(deletedObj, answer);
    for(var x=0 ; x < n ; x++){
        if(deletedObj[x] === 1){
            // console.log(x)
            answer += "X";
        }else{
            answer += "O"
        }
    }
    
    
    return answer;
}