function heappush(heap, elem) {
	heap.push(elem);

	let idx = heap.length - 1;

	while (idx > 0) {
		const parent = Math.trunc((idx - 1) / 2);

		if (heap[idx] < heap[parent]) {
			const temp = heap[parent];

			heap[parent] = heap[idx];
			heap[idx] = temp;
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

		if (heap[left] < heap[next])
			next = left;

		if (right < heap.length && heap[right] < heap[next])
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

		if (heap[left] < heap[next])
			next = left;

		if (right < heap.length && heap[right] < heap[next])
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