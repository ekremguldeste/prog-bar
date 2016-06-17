import sys
import inspect, os
import multiprocessing
import numpy as np
import time



def stamp_versions():
	from scipy.version import version
	import matplotlib
	
	
	# dumps the versions for scipy and numpy in current use
	print "-------- VERSIONS in USE ------------"
	print "Python: ",(sys.version) # parentheses necessary in python 3
	print "SciPy: ",version
	print "Numpy: ",np.version.version
	print "matplotlib: ",matplotlib.__version__
	print "current file name: ", inspect.getfile(inspect.currentframe())
	print "current file directory: ", os.path.dirname(os.path.realpath(__file__))
	print "-------------------------------------"	


def print_there(x, y, text):
     sys.stdout.write("\033[33m\x1b7\x1b[%d;%df%s\x1b8" % (x, y, text))
     sys.stdout.flush()
     return x,y



def progress_bar(pool_count,x_starter_line):
	sys.stdout.write('\33[1m') #bold mode on
	print_there(x_starter_line,0,'Thread #| PID:|______PROGRESS____|  __%|___ ~ EXECUTION PERIOD (hours)|LAUNCHED AT')
	sys.stdout.write('\33[0m') #bold mode off
	
	for i in range (pool_count):

		xcord =print_there(x_starter_line+1+i,0,'Thread '+str(i)+'|') [0] 
		print_there(x_starter_line+1+i,34,'|')
		#print_there(x_starter_line+1+i,55,str([Nspin,B_0,gamma]))
		#sys.stdout.write('\33[16;0H')


def progress_estimator(j,current_xcoord,Nrun1,x_starter_line):
	perprogress=int(np.ceil(float(Nrun1)/20))
	x=j/perprogress
	if j%perprogress==0 and j<Nrun1:
		print_there(x_starter_line+current_xcoord,15+x,'>')

def percentage(current_pid, j, current_xcoord, Nrun1,x_starter_line,launch_time,c_launch_time):	
	if j==25:
		print_there(x_starter_line+current_xcoord,47, str(round((float((time.time()-launch_time))*(Nrun1/25)/3600),3))+'  |'+str(c_launch_time))
		print_there(x_starter_line+current_xcoord,11, str(current_pid))
	if j % 25==0:
		print_there(x_starter_line+current_xcoord, 35, str(round((float(j)/Nrun1)*100,2)))	
	if j == Nrun1-1:
		print_there(x_starter_line+current_xcoord,35, 'completed in'+str(round(float(time.time()-launch_time)/3600,3)))
		#sys.stdout.write('\33['+str(pool_count)+'B')

#___________________________________________________
