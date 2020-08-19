# Definition for a binary tree node.

import sys


frame = list(map(int, sys.stdin.readline().strip().split(" ")))

brick = list(map(int, sys.stdin.readline().strip().split(" ")))

m, n = len(frame), len(brick)

def add_brick(i, brick):
    max_place = frame[i] + brick[0]
    for idx in enumerate(brick):
        if max_place < frame[i+idx] + brick[idx]:



for idx in range(0, m - n):
