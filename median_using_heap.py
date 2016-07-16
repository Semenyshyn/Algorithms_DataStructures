import urllib.request
import heapq


a = urllib.request.urlopen("http://courses.prometheus.org.ua/c4x/KPI/Algorithms101/asset/input_16_10000.txt").read()
a = a.decode("utf-8")
b = list(map(int, a.split()))
b.remove(b[0])


def _heappush_max(heap, item):
    heap.append(item)
    heapq._siftdown_max(heap, 0, len(heap)-1)


def _heappop_max(heap):
    lastelt = heap.pop()
    if heap:
        returnitem = heap[0]
        heap[0] = lastelt
        heapq._siftup_max(heap, 0)
        return returnitem
    return lastelt


def medians_founder(A):
    h_low = [A[0]]
    h_high = []
    for i in A[1:2015]:
        if i <= max(h_low):
            _heappush_max(h_low, i)
        else:
            heapq.heappush(h_high, i)
        if len(h_low) - len(h_high) == 2:
            t = _heappop_max(h_low)
            heapq.heappush(h_high, t)
        if len(h_high) - len(h_low) == 2:
            r = heapq.heappop(h_high)
            _heappush_max(h_low, r)
    return 'low:{0}\n high:{1}\n len_low = {2}\n len_high = {3}'.format(h_low, h_high, len(h_low), len(h_high))