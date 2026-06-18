from multiprocessing import Lock, Process


def send_email(lock:Lock,email:str):
    lock.acquire()
    print(f"send email to {email}")
    lock.release()

if __name__ == '__main__':
    lock = Lock()
    p1 = Process(target=send_email, args=(lock,"user1@test.com"))
    p2 = Process(target=send_email, args=(lock,"user2@test.com"))
    p3 = Process(target=send_email, args=(lock,"user3@test.com"))

    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()