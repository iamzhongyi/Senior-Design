from multiprocessing import Process, Queue
import threading
import time
import sys

def put_more(q):
	i = 0
	while(i < 5):
		output = "input('please enter:')"
		q.put([i, 'P2T2', output])
		time.sleep(0.1)
		i += 1

def f(q,tName):
	q.put([42, None, 'hello'])
	i = 0
	added_thread = threading.Thread(target = put_more, name = tName,args = (q,))
	added_thread.start()
	while(i < 5):
		q.put([i, None, 'hi'])
		print i
		time.sleep(0.1)
		i += 1

if __name__ == '__main__':
    q = Queue()
    p = Process(target = f, args = (q, "P2T2"))
    p.start()
    step = 0
    while(step < 10):
    	print q.get()
    	step += 1
    p.join()