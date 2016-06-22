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

1. Download ```progbar.py ``` and be sure that this file downloaded to the same directory with your ```__main__ ``` code.
2. Import ```time, os, inspect ``` into your main code to let ```progbar``` module stamps the versions of Scipy, Numpy, GCC, current file name and directory and let module estimates the execution time of the code, i.e. 


```python
import time
import sys
import inspect, os 
``` 
3. Then, import ```progbar.py ``` into your main code. 

```python
from progbar import *
```

4. Then call  ``` stamp_versions() ```  for 


# Acknowlegement
Finally, I would like to thank [Burak Kakillioğlu](https://github.com/bkakilli) for enforcing me to upload this module on GitHub
                                                                                            <sup>This work is dedicated to HÖ</sup>
