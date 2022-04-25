function solution(cacheSize, cities) {
    var answer = 0;
    var cacheList = {};
    
    for(var city of cities){
        // console.log(cacheList)
        var cityUpperCase = city.toUpperCase();
        if(cacheList[cityUpperCase] === undefined){
            answer += 5;
            var keyList = Object.keys(cacheList);
            if(cacheSize !== 0 && keyList.length === cacheSize){
                // console.log(keyList)
                var maxKey = keyList.reduce((prev,curr) => {
                    if(cacheList[prev] > cacheList[curr]){
                        return prev;
                    }else{
                        return curr;
                    }
                });
                delete cacheList[maxKey];    
            }
            for(var cache in cacheList){
                cacheList[cache] += 1;
            }
            if(cacheSize !== 0){
                cacheList[cityUpperCase] = 0;    
            }
        }else{
            answer += 1;
            
            cacheList[cityUpperCase] = 0;    
            
            for(var cache in cacheList){
                if(cache !== cityUpperCase){
                    cacheList[cache] += 1;
                }
            }
        }
    }
    
    
    return answer;
}