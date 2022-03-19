function solution(numbers) {
    var answer = -1;
    var sum = numbers.reduce((prev,curr) => prev + curr);
    answer = 45 - sum;
    return answer;
}