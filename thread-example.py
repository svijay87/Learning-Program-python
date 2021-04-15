import time
import threading
import queue

def calc_square(numbers,q):
    print('Calculate the square of number')
    for i in numbers:
        time.sleep(2)
        # Put messages into queue
        q.put(i*i)
        # print(f'\nSquare {i * i}')

def calc_cube(numbers,q):
    print('\nCalculate the cube of number')
    for i in numbers:
        time.sleep(2)
        # Put messages into queue
        q.put(i*i*i)
        # print(f'\ncube {i * i * i}')


if __name__ == "__main__":
    arr = [2, 5, 7, 8]
    q = queue.Queue()
    # Create thread object
    t1 = threading.Thread(name="non-daemon",target=calc_square, args=(arr,q))
    t2 = threading.Thread(name="daemon",target=calc_cube, args=(arr,q))
    # Set t2 thread as Daemon
    t2.daemon = True
    # Invoke the thread
    t1.start()
    t2.start()
    # Now wait for the thread to terminated before proceeding further
    t1.join()
    # t2.join()
    print(f'Queue Size {q.qsize()}')
    # Check if thread is still alive
    print(f'Daemon alive {t2.is_alive()}')

    # Retrieve messages from queue until queue is empty
    while q.empty() is False:
        print(q.get(block=True))

    print('success')
