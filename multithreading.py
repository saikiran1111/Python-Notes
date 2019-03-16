import time
import threading
def square(a):
	for i in a:
		time.sleep(0.2)
		print(i**2)
def cube(a):
	for i in a:
		time.sleep(0.1)
		print(i**3)
a=[3,4,5,6]
t=time.time()
# square(a)
# cube(a)
t1=threading.Thread(target=square,args=(a,))
t2=threading.Thread(target=cube,args=(a,))
t1.start()
t2.start()
t1.join()
t2.join()
print(time.time()-t)