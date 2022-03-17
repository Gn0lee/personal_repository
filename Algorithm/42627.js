function solution(jobs) {
    function heappush(heap, elem) {
        heap.push(elem);

        let idx = heap.length - 1;

        while (idx > 0) {
            const parent = Math.trunc((idx - 1) / 2);

            if (heap[idx][0] < heap[parent][0]) {
                const temp = heap[parent][0];

                heap[parent][0] = heap[idx][0];
                heap[idx][0] = temp;
                idx = parent;
            } else {
                break ;
            }
        }
    }   

    function heappop(heap) {
        const res = heap.shift();

        if (heap.length === 0)
            return res;

        heap.unshift(heap.pop());

        let idx = 0;

        while (idx * 2 + 1 < heap.length) {
            let next = idx;
            const left = idx * 2 + 1;
            const right = idx * 2 + 2;

            if (heap[left][0] < heap[next][0])
                next = left;

            if (right < heap.length && heap[right][0] < heap[next][0])
                next = right;

            if (idx === next)
                break ;

            const temp = heap[idx];

            heap[idx] = heap[next];
            heap[next] = temp;
            idx = next;
        }

        return res;
    }

    function heapify(heap, idx) {
        while (idx * 2 + 1 < heap.length) {
            let next = idx;
            const left = idx * 2 + 1;
            const right = idx * 2 + 2;

            if (heap[left][0] < heap[next][0])
                next = left;

            if (right < heap.length && heap[right][0] < heap[next][0])
                next = right;

            if (idx === next)
                break ;

            const temp = heap[idx];

            heap[idx] = heap[next];
            heap[next] = temp;
            idx = next;
        }
    }

    function buildHeap(heap) {
        for (let idx = Math.trunc((heap.length - 1) / 2); idx >= 0; idx--) {
            heapify(heap, idx);
        }
    }
    
    
    var answer = 0;
    var start = -1;
    var now = 0;
    var heap = [];
    var i = 0;
    const jobsLength = jobs.length;
    
    while(i< jobsLength){
        const currentLength = jobs.length
        for(var j of jobs){
            if(start < j[0] && j[0] <= now){
                heappush(heap,[j[1],j[0]]);
            }
        }
        // console.log(heap, now , "heap에 모음")
        if(heap.length > 0){
            // console.log(heap , "heappop 전")
            var current = heappop(heap);
            // console.log(heap , "heappop")
            start = now;
            now += current[0];
            answer += now - current[1];
            i += 1;
        }else{
            now += 1;
        }
    }
    
    console.log(heap , "종료")
    
    
    return Math.trunc(answer/jobsLength);
}