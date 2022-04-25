function solution(n, k, cmd) {
    var answer = Array.from({length : n}, ()=>"O");
    var deleted = [];
    const Node = function(i,prevNode){
        this.idx = i;
        this.prev = prevNode;
        this.next = null;
    }
    
    var root = new Node(0,null);
    var prev = root;
    var current = root;
    
    for(var i = 1; i < n ; i++){
        var nowNode = new Node(i,prev);
        prev.next = nowNode;
        prev = nowNode;
        
        if(i === k){
            current = nowNode;
        }
    }
    // console.log(current);
    
    for(var currentCmd of cmd){
        var [cmdStr , value] = currentCmd.split(" ");
        switch (cmdStr){
            case "D":
                for(var j = 0 ; j < value ; j++){
                    // console.log(current.next);
                    current = current.next;
                }
            break;
                
            case "C":    
                deleted.push(current);
                // console.log("before C", current);
                var prevNode = current.prev;
                var nextNode = current.next;
                // console.log(current);
                if(prevNode === null){
                    nextNode.prev = null;
                    current = nextNode;
                }else if (nextNode === null){
                    prevNode.next = null;
                    current = prevNode;
                }else{
                    prevNode.next = nextNode;
                    nextNode.prev = prevNode;
                    current = nextNode;
                }

                // console.log("after C", current);
            break;
                
            case "U":
                for(var j = 0 ; j < value ; j++){
                    current = current.prev;
                }
            break;
                
            case "Z":
                var deletedNode = deleted.pop();
                var prevNode = deletedNode.prev;
                var nextNode = deletedNode.next;
                if(prevNode === null){
                    nextNode.prev = deletedNode;
                }else if (nextNode === null){
                    prevNode.next = deletedNode;
                }else{
                    nextNode.prev = deletedNode;
                    prevNode.next = deletedNode;
                }
            break;
        }
    }
    // console.log(deletedObj, answer);
    for(var xNode of deleted){
        answer[xNode.idx] = "X";
    }
    
    
    return answer.join("");
}

console.log(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]));