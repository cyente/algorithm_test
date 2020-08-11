class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        output = []

        def _find(kk, temp):
            if kk == k:
                output.append(temp[:])
                return 0

            for idx in range(temp[-1] + 1, n + 1):
                temp.append(idx)
                _find(kk + 1, temp)
                # temp = temp[:-1]
                temp.pop()
            return

        if k == 0:
            return []
        for idx in range(1, n + 1):
            _find(1, [idx])
        return output

a = Solution()
print(a.combine(4, 3))


# n,m=map(int,raw_input().split())
# n,m=map(int,sys.stdin.readline().strip().split())

# with open('input1.txt', 'r') as f:
#     n, m = map(int, f.readline().strip().split(' '))
#     matrix = [map(int, f.readline().strip().split(' ')) for _ in range(n)]
#     # single line spilt
#
#     temp_list = map(int, f.readline().strip().split(' '))
#     M = temp_list[0]
#     feature_list = [(temp_list[2*idx + 1], temp_list[2*idx+ 2]) for idx in range(M)]
# import sys


import sys
# n,m=map(int,raw_input().split())
# n,m=map(int,sys.stdin.readline().strip().split())
# with open('input2.txt', 'r') as f:
#     # n, m = map(int, f.readline().strip().split(' '))
#     # matrix = [map(int, f.readline().strip().split(' ')) for _ in range(n)]
#     temp = f.readline()
#     while temp:
#         MNlist.append(map(int,temp.strip().split(' ')))
#         temp = f.readline()

