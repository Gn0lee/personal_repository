function solution(n, info) {
    let answer = Array(11).fill(0);
    let max = 0;
    
    function shot(ryan,peach,point,usedShot,arr){
        if(n < usedShot) return
        
        if(point > 10){
            const diff = ryan - peach;
            if(diff > max){
                arr[10] = n - usedShot
                max = diff
                answer = arr
            }
            return
        }
        
        if(n > usedShot){
            let curr = [...arr];
            curr[10-point] = info[10 - point] + 1
            shot(ryan + point, peach , point + 1, usedShot + info[10-point] + 1, curr)
        }
        
        if(info[10-point] > 0){
            shot(ryan, peach + point, point + 1, usedShot, arr)
        }else{
            shot(ryan,peach, point + 1,usedShot, arr)
        }
        
        
    }
    
    shot(0,0,0,0,answer)
    
    return max > 0 ? answer : [-1]
}
