function solution(clothes) {
    // var answer = 0;
    var clothesObj = {};
    var numClothesList = [];
    
    for(var cloth of clothes){
        var [clothName , clothKind] = cloth;
        if(clothesObj[clothKind] === undefined){
            clothesObj[clothKind] = [clothName];
        }else{
            clothesObj[clothKind].push(clothName);
        }
    }
    
    for(var clothesList in clothesObj){
        numClothesList.push(clothesObj[clothesList].length + 1);
    }
    
    return numClothesList.reduce((prev, curr) => prev * curr) - 1;
}