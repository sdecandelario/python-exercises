import concurrent.futures
import random
import threading
import time


def welcome(semaphore, reached_max_users):
    visitor_number = 0
    while not reached_max_users.is_set():
        print(f"welcome visitor #{visitor_number}")
        semaphore.acquire()
        visitor_number += 1
        time.sleep(random.random())


def monitor(semaphore, reached_max_users):
    print(f"[monitor] semaphore={semaphore._value}")
    time.sleep(3)
    if semaphore._value == 0:
        reached_max_users.set()
        print("[monitor] reached max users!")
        print("[monitor] kicking a user out...")
        semaphore.release()
        time.sleep(0.05)
        reached_max_users.clear()


def main():
    reached_max_users = threading.Event()
    semaphore = threading.Semaphore(value=1)
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(welcome, semaphore, reached_max_users)
        executor.submit(monitor, semaphore, reached_max_users)


if __name__ == "__main__":
    main()
