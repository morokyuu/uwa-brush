import time
from threading import Thread

msg = "ok"

def printer():
    global msg
    for _ in range(6):
        time.sleep(1)
        print(f"msg= {msg}")

if __name__ == "__main__":
    print("hello")
    # t = Thread(target=printer,args=(msg,))
    t = Thread(target=printer)
    t.start()
    time.sleep(2.4)
    print("end")
    msg = "uuu"

