function solution(str1, str2) {
    var answer = 0, numUnion = 0, numIntersection = 0;
    
    var specialChr = [ ..." \{\}\[\]\/?.,;:|\)*~`!^\-+<>@\#$%&\\\=\(\'\"0123456789_"];
    
    var str1Counter = {}, str2Counter = {}, union = {}, intersection = {};
    
    str1 = [ ...str1.toUpperCase()];
    
    str2 = [ ...str2.toUpperCase()];
    
    var str1Set = [], str2Set = [];
    
    for(var k = 1 ; k < str1.length ; k ++){
        if(!specialChr.includes(str1[k]) && !specialChr.includes(str1[k-1])){
            str1Set.push(str1[k-1] + str1[k]);
        }
    }
    
    for(var k = 1 ; k < str2.length ; k ++){
        if(!specialChr.includes(str2[k]) && !specialChr.includes(str2[k-1])){
            str2Set.push(str2[k-1] + str2[k]);
        }
    }
    // console.log(str1,str2)
    // console.log(str1Set, str2Set)
    
    for(var i of str1Set){
        if(str1Counter[i] === undefined){
            str1Counter[i] = 1;
        }else{
            str1Counter[i] += 1;
        }
    }
    
    for(var i of str2Set){
        if(str2Counter[i] === undefined){
            str2Counter[i] = 1;
        }else{
            str2Counter[i] += 1;
        }
    }
    
    for(var j of Object.keys(str1Counter)){
        // console.log(j)
        if(str2Counter[j] === undefined){
            union[j] = str1Counter[j];
        }else{
            intersection[j] = Math.min(str1Counter[j], str2Counter[j]);
            union[j] = Math.max(str1Counter[j], str2Counter[j]);
        }
    }
    
    for(var j of Object.keys(str2Counter)){
        if(str1Counter[j] === undefined){
            union[j] = str2Counter[j];
        }
    }
    
    Object.entries(union).forEach(value => numUnion += value[1] );
    Object.entries(intersection).forEach(value => numIntersection += value[1] );
    
    // console.log(numUnion, numIntersection);
    if(str1Set.length === 0 && str2Set.length === 0){
        answer = 65536;
    }else{
        answer = Math.trunc(numIntersection / numUnion * 65536);
    }
    
    return answer;
}