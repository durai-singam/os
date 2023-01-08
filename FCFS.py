# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 13:51:49 2022

@author: J SRI THRISHNA
"""

def waiting_time(processes, bt, wt):
	wt[0] = 0 

	for i in range(1, len(processes)):
		wt[i] = bt[i - 1] + wt[i - 1]


def turn_around_time(processes, bt, wt, tat):
	for i in range(len(processes)):
		tat[i] = bt[i] + wt[i]

def avg_time(processes, bt):
	wt = [0] * len(processes)
	tat = [0] * len(processes) 
	waiting_time(processes, bt, wt)
	turn_around_time(processes, bt, wt, tat)
	total_wt = sum(wt)
	total_tat = sum(tat)
	print("Processes\t", "Burst Time\t", "Waiting time\t", "Turn around time")
	
	for ind, (burst, wait, turn) in enumerate(zip(bt, wt, tat)):
		print(ind, '\t\t', burst, '\t\t', wait, '\t\t', turn)

	print(f"Avg waiting time: {total_wt / len(processes)}")
	print(f"Avg turn around time: {total_tat / len(processes)}")

if __name__ == "__main__":
	processes = [1, 2, 3]
	burst_time = [10, 5, 8]
	avg_time(processes, burst_time)