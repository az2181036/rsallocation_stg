import stg
import numpy as np
import multiprocessing
import server
import constants
import random


def set_stg_env():
    # 多进程(agent)
    pool = multiprocessing.Pool(processes=constants.processing_num)
    # according to mul-arrival_rate lambda compute best_reply、M、s
    # allocate task to service
    pass


def m_m_1():
    task_num = np.linspace(constants.mm1_start_limit, constants.mm1_end_limit, constants.mm1_interval)

    for i in range(len(task_num)):
        for j in range(?):
            num = task_num[i]
            arr_interval = np.random.exponential()
            deal_interval =


def main():
    M,s = stg.best_reply(constants.server_list,constants._lambda)
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