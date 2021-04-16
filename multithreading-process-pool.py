import multiprocessing as mp
import time

def test(fname):
    with open(fname,"w") as f:
        f.write("Hi")
        f.write("Hi 1")
        f.write("Hi 2")
        f.write("Hi 3")
        f.write("Hi 4")


def process_performance(filename):
    start_time = time.time()
    # filename = "text.txt"
    p1 = mp.Process(target=test, args=(filename,))
    p2 = mp.Process(target=test, args=("text-2.txt",))

    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end_time = time.time()
    print(f"Process :: I/O :: Total time taken {end_time - start_time}")


def pool_performance(filename):
    start_time = time.time()
    pool = mp.Pool()
    a = pool.apply_async(test, args=(filename,))
    b = pool.apply_async(test, args=("text-2.txt",))
    a.wait()
    b.wait()
    end_time = time.time()
    print(f"Pool :: I/O :: Total time taken {end_time - start_time}")


if __name__ == "__main__" :
    filename = "text.txt"
    process_performance(filename)
    pool_performance(filename)
