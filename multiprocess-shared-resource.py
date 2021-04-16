from multiprocessing import Process, Manager

def f(d,l):
    d['name'] = 'MP'
    d['purpose'] = 'Shared processs data'
    d['written'] = 'Programmer'
    l.reverse()

if __name__ == "__main__":
    with Manager() as manager:
        d = manager.dict()
        l = manager.list(range(10))

        p = Process(target=f, args=(d,l))
        p.start()
        p.join()

        print(d)
        print(l)