from time import sleep, perf_counter

def task():
    print('Stating a task...')
    sleep(1)
    print('Done')
    
start_time = perf_counter()

task()
task()

end_time = perf_counter()

print(f'it took {end_time - start_time: 0.2f} second(s) to complete.')