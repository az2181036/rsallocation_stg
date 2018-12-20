from constants import ntype

class server():
    def __init__(self, type, process):
        self.type = type
        self.process = process

    def add_this_type_server(self):
        N = [0 for i in range(ntype)]
        N[self.type] = 1
        return N