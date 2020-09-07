# Definition for a binary tree node.

import sys
import math

K, N, M = list(map(int, sys.stdin.readline().strip().split(' ')))
a_list = []
mu_list = []
sigma_list = []
for _ in range(K):
    temp = list(map(float, sys.stdin.readline().strip().split(' ')))
    a_list.append(temp[0])
    mu_list.append(temp[1])
    sigma_list.append(temp[2])
sample_list = list(map(float, sys.stdin.readline().strip().split(' ')))

# with open("czy_input1.txt") as f:
#     K, N, M = list(map(int, f.readline().strip().split(' ')))
#     a_list = []
#     mu_list = []
#     sigma_list = []
#     for _ in range(K):
#         temp = list(map(float, f.readline().strip().split(' ')))
#         a_list.append(temp[0])
#         mu_list.append(temp[1])
#         sigma_list.append(temp[2])
#     sample_list = list(map(float, f.readline().strip().split(' ')))

pi = 3.14159265358979323846264

def Normal(x, mu, sigma):
    return (1. / math.sqrt(2 * pi * sigma**2)) * (math.exp(-(x - mu) ** 2 / (2 * sigma ** 2)))


def EM(a_list, mu_list, sigma_list, sample_list):

    for _ in range(M):
        w = E_step(sample_list, a_list, mu_list, sigma_list)
        a_list, mu_list, sigma_list = M_step(w, sample_list, a_list, mu_list, sigma_list)

    return a_list, mu_list, sigma_list


def E_step(sample_list, a_list, mu_list, sigma_list):
    w = [[0 for _ in range(K)] for _ in range(N)]
    for i in range(N):
        sum_norm = 0.
        for k in range(K):
            # print Normal(sample_list[i], mu_list[k], sigma_list[k])
            sum_norm += a_list[k] * Normal(sample_list[i], mu_list[k], sigma_list[k])
        for k in range(K):
            w[i][k] = a_list[k] * Normal(sample_list[i], mu_list[k], sigma_list[k]) / sum_norm
    return w

def M_step(w, sample_list, a_list, mu_list, sigma_list):
    new_a_list = a_list[:]
    new_mu_list = mu_list[:]
    new_sigma_list = sigma_list[:]

    for k in range(K):
        new_a_list[k] = 0.
        new_mu_list[k] = 0.
        new_sigma_list[k] = 0.
        sumw = 0.
        for i in range(N):
            sumw += w[i][k]
            new_a_list[k] += w[i][k] / float(N)
        for i in range(N):
            new_mu_list[k] += w[i][k] *  sample_list[i] / sumw

        for i in range(N):
            new_sigma_list[k] += w[i][k] * (( sample_list[i] - new_mu_list[k])**2) /sumw

        new_sigma_list[k] = math.sqrt(new_sigma_list[k])
    return new_a_list, new_mu_list, new_sigma_list

a_list, mu_list, sigma_list = EM(a_list, mu_list, sigma_list, sample_list)

for idx in range(K):
    print "%.5f %.5f %.5f" % (a_list[idx], mu_list[idx], sigma_list[idx])


