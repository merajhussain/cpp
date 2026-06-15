import threading
import time

def mythread_task(name:str):
    print("{} start".format(name))
    time.sleep(2)
    print("{} end".format(name))


t1 = threading.Thread(target=mythread_task("A"))
t2 = threading.Thread(target=mythread_task("B"))

t1.start()
t2.start()

t1.join()
t2.join()

