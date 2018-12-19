import math
import queue


num = 100000
rate = [ 82, 10, 57, 14]
_gamma = 10
_lambda = [50,60,70,80,80,100,110,120,130,140,150,160]
process = [82 for i in range(500)] + [57 for i in range(500)] + [14 for i in range(500)] + [10 for i in range(500)]

n = 12
m = 2000

def Best_REPLY(pro, p, _lambda):
    pro.sort(reverse=True)
    k = m - 1

    while True:
        tmp = sum(pro[:k])
        _tmp = 0
        for i in range(k):
            _tmp += math.sqrt(pro[k-i-1])
        t = (tmp - _lambda) / _tmp
        if t >= math.sqrt(pro[k]):
            k = k - 1
        else:
            break

    for j in range(m):
        if j <= k:
            p[j] = (pro[j] - t * math.sqrt(pro[j])) / _lambda
        else:
            p[j] = 0

# def LeaderBestResponse(pro, miu):
#     gamma = _gamma
#     M = [[[0,0,0,0] for i in range(m)] for i in range(gamma)]
#     s = [[0 for i in range(m)] for i in range(gamma)]
#
#     power = sum(pro)
#
#     for i in range(m):
#         k = int(pro[i]/gamma)
#         while k<=power:
#             if s[]



eps = 1e-3
tag = 'Con'
norm = 1
t = [[0] for i in range(n)]
_sum = 0
left = queue.Queue()
right = queue.Queue()
it = 1

s = [[0 for i in range(2000)] for i in range(n)]
p = [[0 for i in range(2000)] for i in range(n)]
final = [0 for i in range(n+1)]

j = 1

while(True):
    if j > 12:
        it += 1
        j = j % 12
    if sum(final) == 12:
        break
    if final[j]:
        j += 1
        continue
    while(True):
        if j == 1:
            if it != 1:
                [norm,it,tag] = left.get()
                if norm < eps:
                    final[1] = 1
                    left.put([norm,it,'STO'])
                    j += 1
                    break
                _sum = 0
                it += 1
        else:
            [_sum, it, tag] = left.get()
            if tag == 'STO':
                final[j] = 1
                if j != m:
                    left.put([_sum, it, 'STO'])
                    j += 1
                break

        for i in range(m):
            tmp = 0
            for k in range(n):
                if k == j-1:
                    continue
                tmp += p[k][i] * _lambda[j-1]
            s[j-1][i] = process[i] - tmp

        Best_REPLY(s[j-1], p[j-1], _lambda[j-1])
        _sumtmp = 0
        for i in range(m):
            tmp = 0
            for k in range(n):
                tmp += p[k][i] * _lambda[j-1]
            _sumtmp += (p[j-1][i]/(process[i]-tmp))

        t[j-1].append(_sumtmp)
        _sum = abs(t[j-1][it-1] - t[j-1][it])
        left.put([_sum,it,'Con'])
        print(_sum,it)
        j += 1
        break

print(_sum,it)
print(p[0])
print(p[1])



