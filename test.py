
from multiprocessing import Manager, Pool
import constants
import os, time, random


def reader(d):
    x = q.get(constants._lambda)
    x[0][0] = x[0][0] * 2
    q.put(x)
    print("reader启动(%s),父进程为(%s)" % (os.getpid(), os.getppid()))
    print(d)


if __name__ == "__main__":
    print("(%s) start" % os.getpid())
    q = Manager().Queue()  # 使用Manager中的Queue来初始化
    d = Manager().dict()
    po = Pool()
    q.put(constants._lambda)
    # 使用阻塞模式创建进程，这样就不需要在reader中使用死循环了，可以让writer完全执行完成后，再用reader去读取
    po.apply(reader, (q,))
    po.apply(reader, (q,))
    po.close()
    po.join()
    print(d)
    print("(%s) End" % os.getpid())