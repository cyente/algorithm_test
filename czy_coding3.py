# Definition for a binary tree node.

import sys

# s = map(str, sys.stdin.readline().strip().split(' '))

# with open('czy_input1.txt', 'r') as f:
n, m = map(int, sys.stdin.readline().strip().split(' '))
edgelist = []
dict_edge = {}
for _ in range(m):
    edgelist.append(map(int, sys.stdin.readline().strip().split(' ')))
    temp = edgelist[-1]
    if dict_edge.has_key(temp[0]):
        dict_edge[temp[0]].append(temp[1])
    else:
        dict_edge[temp[0]] = [temp[1]]

    if dict_edge.has_key(temp[1]):
        dict_edge[temp[1]].append(temp[0])
    else:
        dict_edge[temp[1]] = [temp[0]]

for node in dict_edge.keys():
    dict_edge[node].sort()
    dict_edge[node] = tuple(dict_edge[node])

node_list = dict_edge.keys()
n = len(node_list)
value = 0
for idx in range(n):
    for jdx in range(idx+1, n):
        if dict_edge[node_list[idx]] == dict_edge[node_list[jdx]]:
            value += 1

print value




