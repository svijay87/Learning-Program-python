import os, time
import multiprocessing

results = []

def info(title):
    print(title)
    pid = os.getpid()
    ppid = os.getppid()
    print(f' Module name {__name__} with Parent process {ppid} process id {pid}')

def square(numbers,q):
    info('Funciton Square')
    global results
    print('Calculating the square of numbers')
    for i in numbers:
        time.sleep(3)
        sq = i * i
        q.put(sq)
        results.append(sq)

if __name__ == "__main__":
    q = multiprocessing.Queue()
    arr = [2,3,5,6]
    p1 = multiprocessing.Process(target=square, args=(arr,q))
    p1.start()
    p1.join()

    print(f'Queue size {q.qsize()}')
    while q.empty() is False:
        print(q.get())
    print('Success')