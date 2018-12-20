import math
import queue
import constants

num = 100000
rate = [ 82, 10, 57, 14]
_gamma = 10
_lambda = [50,60,70,80,80,100,110,120,130,140,150,160]
process = [82 for i in range(500)] + [57 for i in range(500)] + [14 for i in range(500)] + [10 for i in range(500)]

n = 12
m = 2000
Qos = 0


def best_reply(pro, p, _lambda):
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

def leader_best_response(p, pro):
    gamma = _gamma
    M = [[[0,0,0,0] for i in range(m)] for i in range(gamma)]
    s = [[0 for i in range(m)] for i in range(gamma)]

    power = sum(p)

    for i in range(m):
        _min_val = math.ceil(p[i]/gamma)
        k = _min_val
        while k <= power:
            if s[k][i-1] < s[k-_min_val] + pro[i]:
                s[k][i] = s[k-_min_val][i-1] + pro[i]
                M[k][i] = M[k-_min_val][i-1] +
            else:
                s[k][i] = s[k][i-1]
                M[k][i] = M[k][i-1]
            k += 1
    return M,s


def stackel_berg_game(pro, miu):
    M,s =
    total_lambda_avg = sum(_lambda) / len(_lambda)
    power = sum(pro)
    k = power / _gamma
    num = sum(M[k][m])
    available_pro = pro.copy()

    while(s[k][m]) <= total_lambda_avg + num/Qos:
        k += 1
        num = sum(M[k][m])

    while(True):


def main():
    M,s = leader_best_response(p, process)


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



