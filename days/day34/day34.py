import time
from collections import deque
import threading


class Scheduler:

    def __init__(self):
        self.q = deque()

    def put_start(self, func):
        self.q.append(func)
    
    def run(self):
        while self.q:
            func = self.q.popleft()
            func()

s  = Scheduler()


def count_up(stop, x=0):
    if x < stop:
       print("countup", x) 
       time.sleep(1)
       s.put_start(lambda: count_up(stop, x+1))
      

def count_down(start):
    if start > 0:
        print("countdown", start)
        time.sleep(1)
        s.put_start(lambda: count_down(start-1))

s.put_start(lambda: count_up(5))
s.put_start(lambda: count_down(5))
s.run()