__author__ = 'aladine'


m = int(raw_input())
line  = map(int,raw_input().strip().split())
s_m = set(line)

n = int(raw_input())
line  = map(int,raw_input().strip().split())
s_n = set(line)
uni = s_m.union(s_n)
inter = s_m.intersection(s_n)
s= list(uni.difference(inter))
s.sort()
for i in s:
    print i
