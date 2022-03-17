function solution(s) {
    const engNumPair = {
        'zero' : '0',
        'one' : '1',
        'two' : '2',
        'three' : '3',
        'four' : '4',
        'five' : '5',
        'six' : '6',
        'seven' : '7',
        'eight' : '8',
        'nine' : '9',  
    }
    
    for(var str in engNumPair){
        var condition = new RegExp(str,"g");
        s = s.replace(condition,engNumPair[str]);
    }
    
    // console.log(s);
    return parseInt(s);
}