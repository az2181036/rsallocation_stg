import stg
import constants

def get_available_process(server_list, p, id):
    tmp = server_list.copy()
    for j in range(constants.m):
        if tmp[j].state is False:
            continue
        for i in range(constants.n):
            if i == id:
                continue
            tmp[j].process -= p[i][j] * constants._lambda[i]
    return tmp


def process_run(q, id):
    while(True):
        p = q.get()
        q.put(p)
        s = get_available_process(constants.server_list, p, id)
        pp = stg.best_reply(s,constants._lambda[id], p[id])
        for i in range(constants.m):
            if p[id][i] - pp[i] > constants.eps:
                flag = True
                p[id][i] = pp[i]
        x = q.get()
        x[id] = p[id]
        q.put(x)
        if flag is not True:
            break


