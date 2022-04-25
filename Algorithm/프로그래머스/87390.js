function solution(n, left, right) {
    var squareArray = Array.from({length : n}, () => 0).map(elem => Array.from({length : n}, () => 0));
    
    for(var i = 0 ; i < n ; i++){
        for(var j = 0 ; j < i + 1; j++){
            squareArray[i][j] = i + 1;
        }
        
        for(var k = i + 1 ; k < n; k ++){
            squareArray[i][k] = k + 1;
        }
    }
    
    var combinedList = squareArray.reduce((prev,curr) => [...prev, ...curr]);
    // console.log(combinedList);
    return combinedList.slice(left,right+1);
}

function solution(n, left, right) {
    var answer = [];
    for(var pos = left ; pos <= right; pos ++){
        const row = Math.trunc(pos / n);
        const column = pos % n;
        
        if(column <= row){
            answer.push(row + 1);
        }else{
            answer.push(column + 1);
        }
    }
    return answer
}