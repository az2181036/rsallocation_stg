import stg
import numpy as np
import multiprocessing
import process
import server
import constants
import random

p = [[0 for i in range(constants.m)] for i in range(constants.n)] # 概率矩阵

def set_stg_env():
    # 多进程(agent)
    pool = multiprocessing.Pool(processes=constants.n)
    manager = multiprocessing.Manager()
    q = manager.Queue(1)
    q.put(p)
    for i in range(constants.n):
        pool.apply_async(process.run,(q,i))
    pool.close()
    pool.join()
    print(p)


def m_m_1():
    task_num = np.linspace(constants.mm1_start_limit, constants.mm1_end_limit, constants.mm1_interval)

    for i in range(len(task_num)):
        for j in range(?):
            num = task_num[i]
            arr_interval = np.random.exponential()
            deal_interval =


def main():
    _lambda = sum(constants._lambda)
    M,s = stg.best_reply(constants.server_list)
    power = stg.get_total_power(constants.server_list)
    k = power/constants._gamma
    num = sum(M[k][constants.m])
    while s[k][constants.m] <= _lambda + num/constants.Qos:
        k = k + power/constants._gamma
        num = sum(M[k][constants.m])
    t = M[k][constants.m]
    # total_lambda_avg = sum(_lambda) / len(_lambda)
    #     # power = sum(p)
    #     # k = power / constants._gamma
    #     # num = sum(M[k][constants.m])
    #     # available_pro = pro.copy()
    #     #
    #     # while (s[k][constants.m]) <= total_lambda_avg + num / constants.Qos:
    #     #     k += 1
    #     #     num = sum(M[k][constants.m])

if __name__ == "__main__":
    main()