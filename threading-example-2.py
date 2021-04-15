from threading import Thread
from threading import Event
import time

class Connection(Thread):
    StopEvent = 0
    def __init__(self,args):
        Thread.__init__(self)
        self.StopEvent = args

    def run(self):
        for i in range(1,10):
            if(self.StopEvent.wait(0)):
                print('Asked to stop')
                break;

            print(f'Child process is sleeping with count {i}')
            time.sleep(3)

        print('Child Thread is exiting')


stop = Event()
conn = Connection(stop)
conn.start()
print('Main Thread is start to wait for 5 sec for Child Thread')
conn.join(5)
print('Main Thread cant wait for more then 5 sec and now stopping the child thread')
stop.set()

conn.join()
print('Main Thread is exiting')