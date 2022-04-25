function solution(numbers, hand) {
    var answer = '';
    const coordinate = {
        0 : [1,0],
        1 : [0,3],
        2 : [1,3],
        3 : [2,3],
        4 : [0,2],
        5 : [1,2],
        6 : [2,2],
        7 : [0,1],
        8 : [1,1],
        9 : [2,1],
    }
    
    var leftPos = [0,0];
    var rightPos = [2,0];
    
    for(var number of numbers){
        switch(number){
            case 1: case 4: case 7:
                answer += "L";
                leftPos = coordinate[number];
            break;
            case 3: case 6: case 9:
                answer += "R";
                rightPos = coordinate[number];
            break;
            case 2: case 5: case 8: case 0:
                const leftD = Math.abs(leftPos[0]-coordinate[number][0]) + Math.abs(leftPos[1]-coordinate[number][1]);
                const rightD = Math.abs(rightPos[0]-coordinate[number][0]) + Math.abs(rightPos[1]-coordinate[number][1]);
                if(leftD === rightD){
                    if(hand === "right"){
                        answer += "R";
                        rightPos = coordinate[number];
                    }else{
                        answer += "L";
                        leftPos = coordinate[number];
                    }
                }else if (leftD < rightD){
                    answer += "L";
                    leftPos = coordinate[number];
                }else{
                    answer += "R";
                    rightPos = coordinate[number];
                }
            break;
        }
    }
    
    return answer;
}