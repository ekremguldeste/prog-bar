# Progress Bar For Multi Processing in Python
```progbar.py ```
module that I created is for monitoring the progress of the processes. Best competible with Monte Carlo (MC) simulations. 





Competible ```Multiporcessing``` functions:
```
* Pool.map()
* Pool.imap()
* Pool.map_async()
* Process
```
![Alt Tex](https://github.com/ekremguldeste/prog-bar/blob/master/progressbar.png)


This piece of algorithm pops up a proggress bar on to your terminal for multiprocessing (can be used with pool.map, pool.imap, pool.map_async, and process) which contains id of your processes, estimated execution time, launch time, percentage of the work done etc.)
Here is the recipe for using it in a proper way!

# Recipe
What you need to do is:

* Download ```progbar.py ``` and be sure that this file downloaded to the same directory with your ```__main__ ``` code.
* Import ```time, os, inspect ``` into your main code to let ```progbar``` module stamps the versions of Scipy, Numpy, GCC, current file name and directory and let module estimates the execution time of the code, i.e. 
```python
import time
import sys
import inspect, os 
``` 
* Then, import ```progbar.py ``` into your main code. 

```python
from progbar import *
```

* Call  ``` stamp_versions() ```  for letting you know the versions of Scipy, Numpy, GCC, current file name and directory :
 
![Alt Tex](https://github.com/ekremguldeste/prog-bar/blob/master/versions.png)

* Lastly you should embed ``` progress_bar(pool_count), progress_estimator(i,current_xcoordinate,Nrun1),  percentage(current_pid, i, current_xcoordinate, Nrun1,launch_time,c_launch_time) ``` correctly to your MC sampler function :
For example let our MC sampler function be ``` run(Nrun1) ```, Then we have,

```python
def run(Nrun1):
	
	global launch_time,c_launch_time
	progress_bar(pool_count)
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
		progress_estimator(i,current_xcoordinate,Nrun1)
		#pops up the percentage, launch date of the code (including year month and day),
		#estimated execution period of the code (your computer will do the job in 'X.XXX'ours)
		percentage(current_pid, i, current_xcoordinate, Nrun1,launch_time,c_launch_time)
		
		#do some complicated work
		time.sleep(0.004)
```

* For a complete **example** here is the [link](https://github.com/ekremguldeste/prog-bar/blob/master/example.py).

# Acknowlegement
Finally, I would like to thank [Burak Kakillioğlu](https://github.com/bkakilli) for enforcing me to upload this module on GitHub.


<sup>This work is dedicated to HÖ.</sup>
