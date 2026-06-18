import os
from multiprocessing import Process, current_process

def send_message(recipient:str):

    print(f"Sending message to {recipient}")
    name=current_process().name
    print(f"message processing successful by the process {name}")


if __name__ == "__main__":
    p1 = Process(target=send_message, args=("name1",))
    p2 = Process(target=send_message, args=("name2",))
    p3 = Process(target=send_message, args=("name3",))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

