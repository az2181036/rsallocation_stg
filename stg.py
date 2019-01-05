import math
import queue
import constants

_lambda = [50,60,70,80,80,100,110,120,130,140,150,160]

def get_total_available_process(server_list, sqrt_flag):
    sum = 0
    if sqrt_flag:
        for i in server_list:
            sum += math.sqrt(i.get_available_process())
    else:
        for i in server_list:
            sum += i.get_available_process()
    return sum

def get_total_power(server_list):
    sum = 0
    for i in range(len(server_list)):
        sum += server_list[i].get_power()

def best_reply(server_list, lambda_j, p):
    server_list.sort(reverse=True)
    k = constants.m - 1

    tmp = get_total_available_process(server_list, False)
    _tmp = get_total_available_process(server_list, True)
    t = (tmp - lambda_j) / _tmp

    while t>= math.sqrt(server_list[k].get_available_process()):
        p[k] = 0
        k = k - 1
        tmp = get_total_available_process(server_list, False)
        _tmp = get_total_available_process(server_list, True)
        t = (tmp - lambda_j) / _tmp

    for j in range(k+1):
        p[j] = (server_list[j].get_available_process() - t * math.sqrt(server_list[j].get_available_process()))/ lambda_j
    return p

def leader_best_response(server_list):
    gamma = constants._gamma
    M = [[[0,0,0,0] for i in range(constants.m)] for i in range(gamma)]
    s = [[0 for i in range(constants.m)] for i in range(gamma)]

    power = get_total_power(server_list)

    for i in range(constants.m):
        _min_val = math.ceil(server_list[i].get_power()/gamma)
        k = _min_val
        while k <= power:
            if s[k][i-1] < s[k - _min_val] + server_list[i].process:
                s[k][i] = s[k-_min_val][i-1] + server_list[i].process
                M[k][i] = M[k-_min_val][i-1] + server_list[i].add_this_type_server()
            else:
                s[k][i] = s[k][i-1]
                M[k][i] = M[k][i-1]
            k += 1
    return M,s

def stackel_berg_game(server_list, qos):

    total_lambda_avg = sum(_lambda) / len(_lambda)
    power = sum(p)
    k = power / constants._gamma
    num = sum(M[k][constants.m])
    available_pro = pro.copy()

    while(s[k][constants.m]) <= total_lambda_avg + num/constants.Qos:
        k += 1
        num = sum(M[k][constants.m])


# tag = 'Con'
# norm = 1
# t = [[0] for i in range(constants.n)]
# _sum = 0
# left = queue.Queue()
# right = queue.Queue()
# it = 1
#
# s = [[0 for i in range(2000)] for i in range(n)]
# p = [[0 for i in range(2000)] for i in range(n)]
# final = [0 for i in range(n+1)]
#
# j = 1
#
# while(True):
#     if j > 12:
#         it += 1
#         j = j % 12
#     if sum(final) == 12:
#         break
#     if final[j]:
#         j += 1
#         continue
#     while(True):
#         if j == 1:
#             if it != 1:
#                 [norm,it,tag] = left.get()
#                 if norm < eps:
#                     final[1] = 1
#                     left.put([norm,it,'STO'])
#                     j += 1
#                     break
#                 _sum = 0
#                 it += 1
#         else:
#             [_sum, it, tag] = left.get()
#             if tag == 'STO':
#                 final[j] = 1
#                 if j != m:
#                     left.put([_sum, it, 'STO'])
#                     j += 1
#                 break
#
#         for i in range(m):
#             tmp = 0
#             for k in range(n):
#                 if k == j-1:
#                     continue
#                 tmp += p[k][i] * _lambda[j-1]
#             s[j-1][i] = process[i] - tmp
#
#         Best_REPLY(s[j-1], p[j-1], _lambda[j-1])
#         _sumtmp = 0
#         for i in range(m):
#             tmp = 0
#             for k in range(n):
#                 tmp += p[k][i] * _lambda[j-1]
#             _sumtmp += (p[j-1][i]/(process[i]-tmp))
#
#         t[j-1].append(_sumtmp)
#         _sum = abs(t[j-1][it-1] - t[j-1][it])
#         left.put([_sum,it,'Con'])
#         print(_sum,it)
#         j += 1
#         break




