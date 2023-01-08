# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 13:23:47 2022

@author: J SRI THRISHNA
"""

from threading import Thread, Semaphore
import random
import time
queue=[]
max_num=10
sem=Semaphore()
class producer(Thread):
    def run(self):
        nums=range(5)
        global queue
        while True:
            sem.acquire()
            if (len(queue)==max_num):
                print("list is full")
                sem.release()
                print("space in queue")
            num=random.choice(nums)
            queue.append(num)
            print("produced",num)
            sem.release()
            time.sleep(random.random())
class consumer(Thread):
    def run(self):
        global queue
        while True:
            sem.acquire()
            if not  queue:
                print("list is empty")
                sem.release()
                print("producer is filling")
            num=queue.pop(0)
            print("consumed",num)
            sem.release()
            time.sleep(random.random())
def main():
    producer().start()
    consumer().start()
if __name__ =="__main__":
    main()
        