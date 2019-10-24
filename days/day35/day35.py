import queue
import time
import threading

def producer(q, count):
    for n in range(count):
        print("Producing", n, n+1)
        q.put(n)
        q.put(n+1)
        time.sleep(1)

    print("Producing Done")
    q.put(None)


def consumer(q):
    while True:
        item = q.get()
        if item is None:
            break
        print("Consuming", item)
    print("Consuming Done")


q = queue.Queue()
threading.Thread(target=producer, args=(q,10)).start()
threading.Thread(target=consumer, args=(q,)).start()