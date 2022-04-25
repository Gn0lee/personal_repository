function solution(s) {
    var answer = [];
    s = s.slice(2,s.length-2);
    var tupleList = s.split("},{");
    
    function compareLength(a , b){
        if(a.length < b.length){
            return -1;
        }
        if(a.length > b.length){
            return 1;
        }
        return 0; 
    }
    
    
    tupleList = tupleList.map((value) => {
        var temp = value.split(",");
        return temp.map((res) => parseInt(res));
        });
    
    tupleList.sort(compareLength);
    
    answer.push(tupleList[0][0]);
    console.log(tupleList);
    tupleList.reduce((prev,curr) => {
        var value = curr.find(elem => !prev.includes(elem));
        answer.push(value);
        return curr;
        // console.log(prev, curr)
    })
    
    return answer;
}