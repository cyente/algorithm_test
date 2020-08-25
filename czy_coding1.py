"""
Question 1:
Given an array with unique integers, "compress" it, so that the minimum value is 1 and the
maximum value is as small as possible.

"Compress" rules:

If before compression, Ai < Aj, then after compression, Ai < Aj

e.g.
[100, 20, 22, 30] -> [4, 1, 2, 3]

format
input: 100, 20, 22, 30
output: 4, 1, 2, 3
"""

import sys

array = map(int, sys.stdin.readline().strip().split(","))

def compress(arr):
    if not arr:
        return arr
    idx_array = zip(*(range(1, len(arr)+1), array))
    idx_array.sort(key=lambda x: x[1])
    _index, _array = zip(*idx_array)
    sort_idx_index = zip(*(range(1, len(arr)+1), _index))
    sort_idx_index.sort(key=lambda x: x[1])
    compress_list, _ = zip(*sort_idx_index)
    return compress_list

print ', '.join(map(str, compress(array)))








