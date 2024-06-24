import threading
from time import sleep

"""
user_input = None


def input_thread():
    global user_input
    user_input = input()


# Start the input thread
input_thread = threading.Thread(target=input_thread)
input_thread.start()
print(user_input)
# Continue executing other tasks
i = 0
while True:

    sleep(1)
    i += 1
    print(i)
    if user_input != None: break
    
    """








if __name__ == '__main__':
    t1 = threading.Thread(target=greet, args=('bob',), daemon=True)
    t2 = threading.Thread(target=greet, args=('alice',), daemon=True)
    t3 = threading.Thread(target=input_thread)
    t1.start()
    t2.start()
    t3.start()
