__author__ = 'aladine'
from operator import itemgetter
from itertools import groupby


def solve(f,l,a,s):
    salut = "Mr." if s=="M" else "Ms."
    print ("%s %s %s" % (salut, f, l))

T = int(raw_input())
list = list()
for x in xrange(T):
    f,l,a,s = raw_input().strip().split()
    list.append([f,l,int(a),s])
list.sort(key=itemgetter(2))
y = groupby(list,itemgetter(2))
for elt, items in y:
    for i in items:
        solve(i[0],i[1],i[2],i[3])
