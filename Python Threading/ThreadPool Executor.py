# from time import sleep, perf_counter

# def task(id):
#     print(f'Starting the task {id}...')
#     sleep(1)
#     return f"Done with task {id}"

# start = perf_counter()

# print(task(1))
# print(task(2))


# finish = perf_counter()
# print(f" It took {finish - start :0.2f} second(s) to finish.")

"""
Using the submit() method example
"""

# from time import sleep, perf_counter
# from concurrent.futures import ThreadPoolExecutor

# def task(id):
#     print(f"Starting the task {id}....")
#     sleep(1)
#     return f"Done with task {id}"

# start = perf_counter()

# with ThreadPoolExecutor() as executor:
#     f1 = executor.submit(task, 1)
#     f2 = executor.submit(task, 2)
    
#     print(f1.result())
#     print(f2.result())
    
# finish = perf_counter()

# print(f"It took {finish-start} second(s) to finish.")

"""
Using the map() method example
"""

from time import sleep, perf_counter
from concurrent.futures import ThreadPoolExecutor


def task(id):
    print(f'Starting the task {id}...')
    sleep(1)
    return f'Done with task {id}'

start = perf_counter()

with ThreadPoolExecutor() as executor:
    results = executor.map(task, [1,2])
    for result in results:
        print(result)

finish = perf_counter()

print(f"It took {finish-start} second(s) to finish.")