from queue import Queue
import random
import time

queue = Queue()

def generate_request():
    unique_id = random.randint(1, 1000)  
    request = f"Request {unique_id}"     
    queue.put(request)                    
    print(f"New request generated: {request}")

def process_request():
    if not queue.empty():            
        request = queue.get()       
        print(f"Processing request: {request}")

        time.sleep(random.uniform(0.5, 2))
        print(f"Request {request} processed.")
    else:
        print("Queue is empty. No requests to process.")

try:
    while True:
        generate_request()      
        process_request()       
        time.sleep(1)   
except KeyboardInterrupt:
    print("Program terminated by user.") 

