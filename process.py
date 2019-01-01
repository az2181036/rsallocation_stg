import stg
import constants
import multiprocessing

def get_available_process(server_list, id):
    tmp = server_list.copy()
    for j in range(constants.m):
        if tmp[j].state is False:
            continue
        for i in range(constants.n):
            if i == id:
                continue
            tmp[j].process -= constants.p[i][j] * constants._lambda[i]
    return tmp

class AgentProcess(multiprocessing.Process):
    def __init__(self, id):
        super(AgentProcess, self).__init__()
        self.id = id

    def run(self):
        while(True):
            s = get_available_process(constants.server_list, self.id)
            p = stg.best_reply(s,constants._lambda[self.id])
            for i in range(constants.m):
                if constants.p[i] - p[i] > constants.eps:
                    flag = True
                    constants.p[i] = p[i]
            if flag is not True:
                break


