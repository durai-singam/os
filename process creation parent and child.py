# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 19:40:35 2023

@author: J SRI THRISHNA
"""

import os
def communication(child_writes):
    r,w=os.pipe()
    processid=os.fork()
    if processid>0:
        os.close(w)
        r=os.fdopen(r)
        print("parent reads")
        str=r.read()
        print("parent is reading",str)
    else:
        os.close(r)
        w=os.fdopen(w,'w')
        print("child writes")
        w.write(child_writes)
        print("Child is writing",child_writes)
        w.close()
str1="Hi this is thrishna"
communication(str1)

import os 
pid=os.fork()
if pid>0:
    print("I am a parent process")
    print("Process id",os.getpid())
    print("child process id",pid)
else:
    print("I am a child process")
    print("process id",os.getpid())
    print("parent process id",os.getppid())

import os 
c=os.fork()
if c>0:
    n=int(input())
    n1,n2=0,1 
    count=0
    if n<=0:
        print("please enter valuable integer")
    elif(n==1):
        print(n)
    else:
        print("fibonacci sequence")
        while count<n:
            print(n1)
            m=n1+n2
            n1=n2
            n2=m
            count+=1 
elif c==0:
    print(None)
    
import os 
a=os.fork()
if a>0:
    b=os.fork()
    if b>0:
        c=os.fork()
        if c>0:
            print("I am parent process")
            print("process id",os.getpid())
        elif c==0:
            print("I am child 1 process")
            print("process id",os.getpid())
            print("parent process id ",os.getppid())
    elif b==0:
        print("I am child 2 process")
        print("process id",os.getpid())
        print("parent process id ",os.getppid())
elif a==0:
    print("I am child 3 process")
    print("process id",os.getpid())
    print("parent process id ",os.getppid())
    
import os 
c=os.fork()
if c>0:
    num=int(input())
    sum=0
    temp=num 
    while temp>0:
        digit=temp%10
        sum+=digit**3
        temp//=10
    if num==sum:
        print(num,"is an armstrong number")
    else:
        print(num,"is not an armstrong number")
elif c==0:
    print(None)