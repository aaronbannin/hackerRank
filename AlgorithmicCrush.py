# https://www.hackerrank.com/challenges/crush

# this solution uses a sparse array
# only record the indicies that have changes
# then traverse list and pull max value
#
# n, m = [int(x) for x in input().strip().split()]
# sparse_array = {}
# max_value = 0
# for i in range(m):
#     op = [int(x) for x in input().strip().split()]
#     for i2 in range(op[0], op[1]+1):
#         old_value = sparse_array.setdefault(i2, 0)
#         new_value = old_value + op[2]
#         sparse_array[i2] = new_value
#         #print(sparse_array)
#         if new_value > max_value:
#             max_value = new_value
#
# print(max_value)

# solves in o(m+n)
"""
because values are stored in order,
and an operation equally impacts all records within a splice
keep track of only the deltas, not total values
after recording all deltas, reduce the array and return max value
"""
n, m = [int(x) for x in input().strip().split()]
values = []
for i in range(n):
    values.append(0)

for M in range(m)
    op = [int(x) for x in input().strip().split()]
    for i in op:
        values[op[0]] += op[2]
        values[op[1]] -= op[2]

running = 0
max_value = 0
for record in values:
    running += record
    if running > max_value:
        max_value = running

print(max_value)
