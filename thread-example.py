import time
import threading
import queue


def calc_square(numbers,q):
    print('Calculate the square of number')
    for i in numbers:
        time.sleep(2)
        q.put(i*i)
        # print(f'\nSquare {i * i}')

def calc_cube(numbers,q):
    print('\nCalculate the cube of number')
    for i in numbers:
        time.sleep(2)
        q.put(i*i*i)
        # print(f'\ncube {i * i * i}')


if __name__ == "__main__":
    arr = [2, 5, 7, 8]
    q = queue.Queue()
    t1 = threading.Thread(target=calc_square, args=(arr,q))
    t2 = threading.Thread(target=calc_cube, args=(arr,q))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(f'Queue Size {q.qsize()}')
    while q.empty() is False:
        print(q.get())
    print('success')