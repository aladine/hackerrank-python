def quicksort(seq):
  if len(seq) <= 1: 
    return seq
  lo, pivot, hi = partition(seq)
  return quicksort(lo) + [pivot]+ quicksort(hi)

def partition(seq):
  pi, seq = seq[0], seq[1:]
  lo = [x for x in seq if x<= pi]
  hi = [x for x in seq if x> pi]
  return lo, pi, hi

arr = [0,2,3,4,2,1,9]
print quicksort(arr)
#print arr
