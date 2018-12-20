import constants

class server(object):
    def __init__(self, type, idle_power, busy_power, process, util = 0):
        self.type = type
        self.idle_power = idle_power
        self.busy_power = busy_power
        self.process = process
        self.utilazation = util

    def __lt__(self, other):
        return self.process < other.process

    def __eq__(self, other):
        return self.process < other.process

    def __str__(self):
        return str(self.process)

    def add_this_type_server(self):
        N = [0 for i in range(constants.ntype)]
        N[self.type] = 1
        return N

    def set_utilaztion(self, miu):
        self.utilazation = miu / self.process

    def get_power(self):
        return self.idle_power + self.utilazation * (self.busy_power - self.idle_power)
