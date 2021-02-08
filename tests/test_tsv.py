import threading
import time
import inspect
import unittest

from threadsafevariable import ThreadSafeVariable


class A(object):
    x = ThreadSafeVariable()

    def __init__(self, x):
        self.x = x
        ThreadSafeVariable._image = ThreadSafeVariable.freeze()

    def restore(self):
        ThreadSafeVariable.restore(ThreadSafeVariable._image)


class MyThread(threading.Thread):
    def run(self):
        assert self.a.x == 3
        self.a.x = 5
        time.sleep(0.2)
        assert self.a.x == 5


class MyTest(unittest.TestCase):
    def test_tsv(self):
        a = A(4)
        b = A(2)
        a.x = 3
        t = MyThread()
        t.a = a
        t.start()
        time.sleep(0.3)
        assert a.x == 3
        t.join()
        assert b.x == 2
        a.restore()
        assert a.x == 4
        a.x = 3
        t = MyThread()
        t.a = a
        t.start()
        time.sleep(0.3)
        assert a.x == 3
