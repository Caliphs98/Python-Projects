# from threading import Event, Thread
# from time import sleep

# def task(event: Event, id:int) -> None:
#     print(f'Thread {id} started. Waiting for the signal.....')
#     event.wait()
#     print(f'Received signal. The thread {id} was completed.')
    
# def main() -> None:
#     event = Event()
    
#     t1 = Thread(target=task, args=(event,1))
#     t2 = Thread(target=task, args=(event,2))
    
#     t1.start()
#     t2.start()
    
#     print('Blocking the main thread for 3 seconds...')
#     sleep(3)
#     event.set()



# if __name__ == '__main__':
#     main()

"""
Practical example of using Threading event
"""
from threading import Thread, Event
from urllib import request


def download_file(url, event):
    # Download the file from URL
    print(f'Downloading  file from {url}....')
    filename, _ = request.urlretrieve(url, "rfc793.txt")
    
    # File download completed, set the event
    event.set()
    
def process_file(event):
    print("Waiting for the file to be download....")
    event.wait() # Wait for the event to be set
    
    # File has been downloaded, start processing it
    print("File download complete. Starting file processing...")
    
    # Count the nummber of words in the file
    word_count = 0
    with open("rfc793.txt", 'r') as file:
        for line in file:
            words = line.split()
            word_count += len(words)
            
    # Print the word count
    print(f'Number of words in the file: {word_count}')
    


def main():
    # Create an Event object
    event = Event()
    
    
    # Create and start the file download thread
    download_thread = Thread(target=download_file,
                             args=("https://www.ietf.org/rfc/rfc793.txt", event))
    
    
    download_thread.start()
    
    
    # Create and start the file processing thread
    process_thread = Thread(target=process_file, args=(event,))
    
    process_thread.start()
    
    
    # Wait for threads to complete
    download_thread.join()
    process_thread.join()
    
    print("Main thread finished.")
    

if __name__ == '__main__' :
    main()
    