import time
import threading
import concurrent.futures
import multiprocessing

start = time.perf_counter()


def do_something(second):
    print("Sleeping")
    time.sleep(second)
    return second


if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        results = executor.map(do_something, secs)
        for result in results:
            print(result)
    finish = time.perf_counter()
    print(f"Finished in {round(finish-start,2)} seconds")
