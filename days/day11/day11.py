from functools import total_ordering
import queue
import threading


@total_ordering
class Job:
    def __init__(self, priority: int, description: str) -> None:
        self.priority = priority
        self.description = description

    def __eq__(self, other) -> bool:
        try:
            return self.priority == other.priority
        except AttributeError:
            return NotImplemented

    def __lt__(self, other) -> bool:
        try:
            return self.priority < other.priority
        except AttributeError:
            return NotImplemented


q = queue.PriorityQueue()

q.put(Job(10, "Third-level job"))
q.put(Job(3, "One-level job"))
q.put(Job(5, "Second-level job"))


def process_job(q):
    while True:
        next_job = q.get()
        print("process_job", next_job.description)
        q.task_done()


works = [
    threading.Thread(target=process_job, args=(q,)),
    threading.Thread(target=process_job, args=(q,)),
]
for work in works:
    work.setDaemon(True)
    work.start()

q.join()
