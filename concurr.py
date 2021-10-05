from concurrent.futures import *
import time

start = time.perf_counter()


def do_something(seconds):
    print(f'Dormindo {seconds} segundo(s)...')
    time.sleep(seconds)
    return f'Parou de dormir...{seconds} sec'


with ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = [executor.submit(do_something, sec) for sec in secs]
    
    for f in as_completed(results):
        print(f.result())

finish = time.perf_counter()

print(f'Terminou em {round(finish-start, 2)} segundo(s).')