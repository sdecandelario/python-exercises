import time
import threading


def myfunc1(name):
    print(f"myfunc1 started with {name}")
    time.sleep(10)
    print("myfunc1 ended")


def myfunc2(name):
    print(f"myfunc2 started with {name}")
    time.sleep(10)
    print("myfunc2 ended")


def myfunc3(name):
    print(f"myfunc3 started with {name}")
    time.sleep(10)
    print("myfunc3 ended")


def main():
    print("main started")
    t1 = threading.Thread(target=myfunc1, args=["foo"])
    t2 = threading.Thread(target=myfunc2, args=["bar"])
    t3 = threading.Thread(target=myfunc3, args=["baz"])

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
    print("main ended")


if __name__ == "__main__":
    main()
