from collections import deque

def is_palindrome(string):
    
    string = string.lower().replace(" ", "")
    
    queue = deque(string)
    

    while len(queue) > 1:
        if queue.popleft() != queue.pop():
            return False
    return True

