# from threading import Thread
# from time import sleep

# counter = 0

# def increase(by):
#     global counter
    
#     local_counter = counter
#     local_counter += by
    
#     sleep(0.1)
    
#     counter = local_counter
#     print(f'counter={counter}')
    
    
# # create threads
# t1 = Thread(target=increase, args=(10,))
# t2 = Thread(target=increase, args=(20,))

# # start the threads
# t1.start()
# t2.start()

# # waiting for the threads to complete
# t1.join()
# t2.join()


# print(f'The final counter is {counter}')

"""
Using a threading lock to prevent the race condition
"""

# from threading import Thread, Lock
# from time import sleep


# counter = 0

# def increase(by, lock):
#     global counter
    
#     lock.acquire()
    
#     local_counter = counter
#     local_counter += by

#     sleep(0.1)

#     counter = local_counter
#     print(f'counter={counter}')
    
#     lock.release()
    
# lock = Lock()

# # create threads
# t1 = Thread(target=increase, args=(10, lock))
# t2 = Thread(target=increase, args=(20, lock))

# # start the threads
# t1.start()
# t2.start()

# # wait for the threads to complete
# t1.join()
# t2.join()

# print(f'The final counter is {counter}')

"""
Using the threading lock with the with statement
"""

# from threading import Thread, Lock
# from time import sleep


# counter = 0

# def increase(by, lock):
#     global counter

#     with lock:
#         local_counter = counter
#         local_counter += by

#         sleep(0.1)

#         counter = local_counter
#         print(f'counter={counter}')


# lock = Lock()

# # create threads
# t1 = Thread(target=increase, args=(10, lock))
# t2 = Thread(target=increase, args=(20, lock))

# # start the threads
# t1.start()
# t2.start()


# # wait for the threads to complete
# t1.join()
# t2.join()


# print(f'The final counter is {counter}')

"""
Defining thread-safe Counter class that uses threading Lock object

"""
from threading import Thread, Lock
from time import sleep

class Counter:
    def __init__(self):
        self.value = 0
        self.lock = Lock()
        
    def increase(self,by):
        with self.lock:
            current_value = self.value
            current_value += by
            
            sleep(0.1)
            
            self.value = current_value
            print(f'counter={self.value}')
            
def main():
    counter =Counter()
    # create threads
    t1 = Thread(target=counter.increase, args=(10,))
    t2 = Thread(target=counter.increase, args=(20,))

    # start the threads
    t1.start()
    t2.start()


    # wait for the threads to complete
    t1.join()
    t2.join()
    
    print(f'The final counter is {counter.value}')
    
if __name__ == '__main__':
    main()