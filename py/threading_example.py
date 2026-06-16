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

counter =0
def critical_section_code(task:str):
    global counter
    lock = threading.Lock()
    lock.acquire()
    counter += 1
    lock.release()
    print("Thread {} updated counter value to {}".format(task,counter))

t3 = threading.Thread(target=critical_section_code("task C"))
t4 = threading.Thread(target=critical_section_code("task D"))


t1.join()
t2.join()


t3.start()
t4.start()
t3.join()
t4.join()