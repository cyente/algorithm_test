# Definition for a binary tree node.

import sys
import math


with open("czy_input1.txt") as f:
    K, N, M = list(map(int, f.readline().strip().split(' ')))
    a = []
    mu = []
    sigma = []
    for _ in range(K):
        temp = list(map(float, f.readline().strip().split(' ')))
        a.append(temp[0])
        mu.append(temp[1])
        sigma.append(temp[2])
    sample_list = list(map(float, f.readline().strip().split(' ')))


def 

def EM(a, mu, sigma, sample_list):



def E_step():
