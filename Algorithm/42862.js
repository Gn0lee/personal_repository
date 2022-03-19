function solution(n, lost, reserve) {
    var answer = 0;
    
    for(var lostman of lost){
        var checkLost = reserve.indexOf(lostman);
        if(checkLost !== -1){
            reserve.splice(checkLost,1);
            lost = lost.filter(value => value !== lostman);
        }
    }
    
    answer += n - lost.length;
    if(lost.includes(1) && reserve.includes(2)){
        answer += 1;
        lost.splice(lost.indexOf(1),1);
        reserve.splice(reserve.indexOf(2),1);
    }
    if(lost.includes(n) && reserve.includes(n-1)){
        answer += 1;
        lost.splice(lost.indexOf(n),1);
        reserve.splice(reserve.indexOf(n-1),1);
    }
    
    for(var lostman2 of lost){
        // console.log(lostman2)
        if(reserve.includes(lostman2 - 1)){
            reserve = reserve.filter(value => value !== lostman2 - 1);
            answer += 1;
        }else if (reserve.includes(lostman2 + 1)){
            reserve = reserve.filter(value => value !== lostman2 + 1);
            answer += 1;
        }
    }
    
    return answer;
}