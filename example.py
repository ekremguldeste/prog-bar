from scipy.integrate import ode,odeint
import numpy as np
import matplotlib.pyplot as plt
import time
import sys
import inspect, os



#import progressbar
from progbar import *
pool_count=12
#params
Nrun1=2000 # total run count
x_starter_line=10 # this is the y coordinate where your progresbar shows up
stamp_versions() # stamps the versions of Scipy, Numpy, GCC, current file name and directory




def run(Nrun1):
	
	global launch_time,c_launch_time
	progress_bar(pool_count,x_starter_line)
	#import the times when the code first launched
	launch_time=time.time()
	c_launch_time=time.ctime()
	
	#multiprocessing in queue (to use other module comment the line below)
	q.put([Nrun1])
	
	for i in range (Nrun1):
	
		#your current process:
		current = multiprocessing.current_process()
		#current coordinate of your cursor
		current_xcoordinate=current._identity[0]
		#current process id
		current_pid=os.getpid()
		#puts '>' when some Nrun1/25 of the job completed
		progress_estimator(i,current_xcoordinate,Nrun1,x_starter_line)
		#pops up the percentige, launch date of the code (including year month and day), estimated execution period of the code (your computer will do the job in 'X.XXX'ours)
		percentage(current_pid, i, current_xcoordinate, Nrun1,x_starter_line,launch_time,c_launch_time)
		
		#do some complicated work
		time.sleep(0.004)

#stuff for multi processing

from multiprocessing import Pool,Process,Queue


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




