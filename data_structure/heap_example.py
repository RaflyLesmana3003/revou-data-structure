import heapq as heapppp

heap = []
heapppp.heapify(heap)

heapppp.heappush(heap, 109)
heapppp.heappush(heap, 288)
heapppp.heappush(heap, 10)
heapppp.heappush(heap, 20)
heapppp.heappush(heap, 100)

heapppp._heapify_max(heap)

# remove and get smallest element from the heap
removed_node = heapppp.heappop(heap)
print(removed_node)

removed_node = heapppp.heappop(heap)
print(removed_node)

