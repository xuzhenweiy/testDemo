import threading
import time


class ThreadingTest(object):

    def __init__(self):
        self.count = 0

        #调用Lock方法 当函数执行完之后才执行下1个线程
        self.lock = threading.Lock()

    def printData(self,id):

        #锁定线程
        self.lock.acquire()

        time.sleep(0.2)

        self.count +=1
        print('id=',id,'count=',self.count)

        #释放线程
        self.lock.release()



    def execute_thread(self):

        for i in range(10):

            #调用多线程方法 传入执行的函数,参数
            print("执行多线程")
            t = threading.Thread(target=self.printData,args=(i,))
            t.start()



instance = ThreadingTest().execute_thread()

