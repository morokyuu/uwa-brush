import time
from threading import Thread

def printer():
    for _ in range(5):
        time.sleep(1)
        print("ok")

if __name__ == "__main__":
    print("hello")
    t = Thread(target=printer)
    t.run()
