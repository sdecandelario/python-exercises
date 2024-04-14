import time
import threading


def myfunc(name):
    print(f"myfunc started with {name}")
    time.sleep(10)
    print("myfunc ended")


def main():
    print("main started")
    t = threading.Thread(target=myfunc, args=["foo"], daemon=True)
    t.start()
    print("main ended")


if __name__ == "__main__":
    main()
