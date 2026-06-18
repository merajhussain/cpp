import asyncio
import time
from multiprocessing import Pool, Lock,Process

def worker(task_name:str):
    print(f"worker started {task_name}")
    time.sleep(2)
    print(f"worker finished {task_name}")

if __name__ == '__main__':
    task_names=["t1", "t2", "t3", "t4"]
    pool = Pool(processes=4)
    print(pool.map(worker,task_names))

