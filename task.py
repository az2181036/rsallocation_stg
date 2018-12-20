import time

class task(object):
    def __init__(self, _lambda):
         self.borntime = time.perf_counter()
         self._lambda = _lambda
         self.runtime = 0
         self.endtime = 0

    def get_runtime(self):
        self.endtime = time.perf_counter()
        self.runtime = self.endtime - self.borntime

