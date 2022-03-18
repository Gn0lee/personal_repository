function solution(board, moves) {
    var answer = 0;
    var bascket = [];
    const totalLength = board.length;
    var currentHeight = {};
    
    for(var j = totalLength -1 ; j > -1 ; j --){
        for(var i = 0 ; i < totalLength; i ++){
            if(board[j][i] === 0 && currentHeight[i] === undefined){
                currentHeight[i] = totalLength - j - 1;
            }
        }   
    }

    for(var k = 0 ; k < totalLength; k++){
        if(currentHeight[k] === undefined){
            currentHeight[k] = totalLength;
        }
    }
    
    for(var picker of moves){
        // console.log(currentHeight,board);
        if(currentHeight[picker-1] !== 0){
            var pickedIndex = totalLength - currentHeight[picker-1];
            // console.log(pickedIndex);
            var pickedDoll = board[pickedIndex][picker-1];
            
            if(bascket[bascket.length-1] === pickedDoll){
                answer += 2;
                bascket.pop();
            }else{
                bascket.push(pickedDoll);
            }
            board[totalLength - currentHeight[picker-1]][picker-1] = 0;
            currentHeight[picker-1] -= 1;
        }
    }
    
    return answer;
}

console.log(solution([[1, 0, 0], [1, 0, 0], [1, 0, 0]],[1,1,1]))