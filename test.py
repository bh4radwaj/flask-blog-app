import os
import time
from threading import Thread
from multiprocessing import Process

count = 0

def sleep():
    global count
    time.sleep(5)
    count+=1
    print(count,":",str(os.getpid()))

process = []
for i in range(50):
    t = Process(target=sleep,args=())
    process.append(t)
for proc in process:
    proc.start()


