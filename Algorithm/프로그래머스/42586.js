function solution(progresses, speeds) {
    var answer = [];
    const prgLength = progresses.length;
    var timeList = [];
    
    for(var i = 0 ; i < prgLength ; i ++){
        var time = Math.ceil((100 - progresses[i])/speeds[i]);
        timeList.push(time);
    }
    
    while(timeList.length > 0){
        var now = timeList.shift();
        var temp = 1;
        
        while(timeList[0] <= now){
            temp += 1;
            timeList.shift();
        }
        answer.push(temp);
    }
    
    return answer;
}