from multiprocessing import Process,Queue
import random
import queue

def f(q):
    q.put(['thrishna','23',"jayakumar"])
def main():
    q=Queue()
    p=Process(target=f,args=(q,))
    p.start()
    print(q.get())
if __name__ == "__main__":
    main()

from multiprocessing import Process,Pipe

def f(conn):
    conn.send(['thrishna','23','jayakumar'])
    conn.close()
if __name__ =="__main__":
    parent_conn,child_conn=Pipe()
    p=Process(target=f,args=(child_conn,))
    p.start()
    print(parent_conn.recv())
    p.join()

import multiprocessing

def print_records(records):
    for record in records:
        print("Name :{0} \nScore:{1}\n".format(record[0],record[1]))
def insert_record(record,records):
    records.append(record)
    print(" A New record is added")
if __name__ =="__main__":
    with multiprocessing.Manager() as manager:
        records=manager.list([('thrishna','99'),("sanajay","100"),('kavitha','98')])
        new_records=("jayakumar",'78')
        p1=multiprocessing.Process(target=insert_record,args=(new_records,records))
        p2=multiprocessing.Process(target=print_records,args=(records,))
        p1.start()
        p1.join()
        p2.start()
        p2.join()

from multiprocessing import Process, Value, Array

def f(n, a):
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] = -a[i]

if __name__ == '__main__':
    num = Value('d', 0.0)
    arr = Array('i', range(10))

    p = Process(target=f, args=(num, arr))
    p.start()
    p.join()

    print(num.value)
    print(arr[:])



