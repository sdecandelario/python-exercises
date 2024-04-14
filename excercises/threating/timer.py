import threading


def boom():
    print("BOOM!")


def main(interval=5):
    timer = threading.Timer(interval, boom)
    timer.start()
    import time

    time.sleep(3)


if __name__ == "__main__":
    main(1)
