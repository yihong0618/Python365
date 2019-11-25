from threading import Thread
import time


def print_n(n):
    time.sleep(n)
    print(n)


def makethread_group(n):
    print_n(n)
    if n == 2:
        print_n(n+1)

t1 = Thread(target=makethread_group, args=(6,))
t2 = Thread(target=makethread_group, args=(2,))
[t1.start(), t2.start()]