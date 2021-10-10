#%%
import time
from threading import Thread

def sleeper(i):
    print("Thread {0} sleeps for 5 seconds".format(i))
    time.sleep(5)
    print("Thread {0} woke up".format(i))
    
for i in range(10):
    t =Thread(target=sleeper, args=(i,))
    t.start()

