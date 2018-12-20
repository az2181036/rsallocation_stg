from server import server

eps = 1e-3

n = 12 # agent 数量
m = 2000 # 服务器数量
ntype = 4 # 服务器种类

ntask = 10000 # 任务数量

rate = [ 82, 10, 57, 14] # 种类对应的处理速率
Qos = 0 # avg response time

# 服务器列表
server_list = [server(0,49.6,272,82) for i in range(500)] + [server(1,15.9,45.1,10) for i in range(500)] + \
          [server(2,122,580,57) for i in range(500)] + [server(3,63.2,236,14) for i in range(500)]

_lambda = []  # 到达速率 for n agents
_gamma = 0 # 分级的数目


