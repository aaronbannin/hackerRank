# https://www.hackerrank.com/challenges/append-and-delete?h_r=next-challenge&h_v=zen

s = input()
t = input()
k = int(input())

if s == t and k%2 == 0:
    print('Yes')
elif len(s) + len(t) < k:
    print('Yes')
elif len(s) > len(t):
    s_1 = s
    while s_1 != t[:len(s_1)]:
        s_1 = s_1[:len(s_1)-1]

    actions_taken = len(s) - len(s_1)
    actions_needed = len(t) - len(s_1)
    if actions_taken + actions_needed == k:
        # have exactly the remaining actions
        print('Yes')
    else:
        print('No')

elif len(s) < len(t):
    if len(t) - len(s) == k:
        # i can just add the needed letters
        print('Yes')
    else:
         pass
