function solution(record) {
    var answer = [];
    var commandList = [];
    var idNickPair = {};
    
    for(var curRecord of record){
        var [command, id, nickname] = curRecord.split(" ");
        
        switch (command){
            case "Enter":            
                idNickPair[id] = nickname;
                commandList.push([command,id]);
            break;
                
            case "Leave":
                commandList.push([command,id]);
            break;
                
            case "Change":
                idNickPair[id] = nickname;
            break;
        }
    }
    
    for(var [curCommand, curId] of commandList){
        if(curCommand === "Enter"){
            answer.push(idNickPair[curId]+"님이 들어왔습니다.");
        }else{
            answer.push(idNickPair[curId]+"님이 나갔습니다.");
        }
    }
    
    
    
    return answer;
}