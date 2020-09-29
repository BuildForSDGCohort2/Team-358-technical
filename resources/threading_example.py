import threading
import time


# Creating the first function
def first_function():
    print("First hello from the first thread")
    time.sleep(4)
    print("Second hello from the first thread")
    time.sleep(4)


# Creating the second function
def second_function():
    print("First hello from the second thread")
    time.sleep(4)
    print("Second hello from the second thread")
    time.sleep(4)


# Create threads
# x = threading.Thread(target=first_function, args=())
x1 = threading.Thread(target=first_function)
x2 = threading.Thread(target=second_function)

# Creating our thread object
x1.start()
x2.start()
