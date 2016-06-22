from scipy.integrate import ode,odeint
import numpy as np
import matplotlib.pyplot as plt
import time
import sys
import math as m
import inspect, os
import multiprocessing
pool_count=12
from progbar import *

#params
Nrun1=2000 # total run count
x_starter_line=10 # this is the y coordinate where your progresbar shows up
stamp_versions()




def run(Nrun1):
	
	global launch_time,c_launch_time
	progress_bar(12,x_starter_line)
	launch_time=time.time()
	c_launch_time=time.ctime()
	
	#multiprocessing in queue
	q.put([Nrun1])
	
	for i in range (Nrun1):
	

		current = multiprocessing.current_process()
		current_xcoordinate=current._identity[0]
		current_pid=os.getpid()
		progress_estimator(i,current_xcoordinate,Nrun1,x_starter_line)
		percentage(current_pid, i, current_xcoordinate, Nrun1,x_starter_line,launch_time,c_launch_time)
		
		#do some complicated work
		time.sleep(0.004)



from multiprocessing import Pool,Process,Queue
#pool=Pool(pool_count)
#result = pool.map(run,[Nrun1]*pool_count)
#result = pool.map_async(run,[Nrun1]*pool_count)
#result = pool.imap(run,[Nrun1]*pool_count)
#hosts = [Nrun1]*pool_count
#args = ((host) for host in hosts)
#pool = Pool(processes=pool_count)
#pool.map_async(run, args)
#pool.close()
#pool.join()

def mmap():
	pool = Pool(pool_count)
	result = pool.map(run, [Nrun1]*pool_count)
	pool.close()
	pool.join()

def mmap_asn():
	pool=Pool(pool_count)
	result = pool.map_async(run, [Nrun1]*pool_count)
	pool.close()
	pool.join()
def immap():
	pool = Pool(pool_count)
	result = pool.imap(run, [Nrun1]*pool_count)
	pool.close()
	pool.join()


def proc():
	jobs = []
	global q
	for i in range(pool_count):
		q = Queue()
		p = Process(target=run, args=(Nrun1,))
		jobs.append(p)	
		p.start()
		q.get()

	p.join()


proc()
#mmap()
#mmap_asn()
#immap()




