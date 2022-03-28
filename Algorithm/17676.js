function solution(lines) {
    var answer = 0;
    var timeList = [];
    var startEnds = [];
    for(var line of lines){
        var [date , time, range] = line.split(" ");
        var diff = Number(range.slice(0,range.length-1)) * 1000 - 1;
        // console.log(diff);
        var endTime = new Date(date + " " + time).getTime();
        var startTime = endTime - diff;
        // console.log(startTime, endTime)
        timeList.push(startTime, endTime);
        startEnds.push([startTime,endTime]);
    }
    
    var tmp = 0;
    
    for(var start of timeList){
        var end = start + 999;
        // console.log("start : ",start, "end : ",end);
        for(var i = startEnds.length-1 ; i > -1 ; i--){
            var[s,e] = startEnds[i];
            
            if((e >= start && s <= end) || (s <= end && e >= start)){    
                // console.log("s : ", s, "e : ",e);
                tmp += 1;
            }else if(e < start){
                break;
            }
        }
        answer = Math.max(answer, tmp);
        tmp = 0;
    }
    
    
    return answer;
}