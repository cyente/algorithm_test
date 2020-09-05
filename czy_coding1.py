import sys

n = int(sys.stdin.readline().strip())
use_info = []
for _ in range(n):
    use_info.append(sys.stdin.readline().strip().split(' '))
# with open('czy_input1.txt', 'r') as f:
#     n = int(f.readline().strip())
#     use_info = []
#     for _ in range(n):
#         use_info.append(f.readline().strip().split(' '))


dict_username = {}

for idx in range(n):
    if dict_username.has_key(use_info[idx][1]):
        dict_username[use_info[idx][1]].add(use_info[idx][0])

    else:
        dict_username[use_info[idx][1]] = set([use_info[idx][0]])

sum = 0
for key, value in dict_username.items():
    if len(value) >=2:
        sum += len(value)

print sum





