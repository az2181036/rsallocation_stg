import time

class task(object):
    def __init__(self,  id, _lambda, runtime):
        self.id = id
        self.borntime = time.perf_counter()
        self._lambda = _lambda
        self.start_time = 0
        self.endtime = 0

    def set_start_time(self):
        self.start_time = time.perf_counter()

    def get_runtime(self):
        self.endtime = time.perf_counter()
        return self.endtime - self.start_time

    def get_wait_time(self):
        return self.start_time - self.borntime