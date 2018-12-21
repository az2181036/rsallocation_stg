import stg
import server
import constants
import random

def main():
    M,s = stg.best_reply(constants.server_list,constants._lambda)
    # total_lambda_avg = sum(_lambda) / len(_lambda)
    # power = sum(p)
    # k = power / constants._gamma
    # num = sum(M[k][constants.m])
    # available_pro = pro.copy()
    #
    # while (s[k][constants.m]) <= total_lambda_avg + num / constants.Qos:
    #     k += 1
    #     num = sum(M[k][constants.m])

if __name__ == "__main__":
    main()