# test for usage of multithread
import sys
import threading
import time
def thread_job(input):
	print('start')
	for i in xrange(10):
		time.sleep(0.1)
	print('finish processing:' + input + '\n')

def main ():
	stringtype = ''
	while(stringtype != 'quit'):
		stringtype = input('please enter:')
		added_thread = threading.Thread(target = thread_job,name = 'T1',args = (stringtype,))
		added_thread.start()
		#print(threading.active_count()) # see how many active threads
		print(threading.enumerate()) # who are they
	#added_thread.join()
	print('all done\n')
	print(threading.enumerate())

if __name__ == '__main__':
	main()

