def sort(names):
    bucket = [ 0 for _ in xrange(26)]
    for name in names:
        c = ord(name.lower()[0]) - ord('a')
        bucket[c] += 1

    print bucket    

    for i in xrange(1,26):
        bucket[i] += bucket[i-1]
    print bucket    
    
    new_array = ['' for _ in names]
    for name in names:
        c = ord(name.lower()[0]) - ord('a')
        
        new_index = bucket[c]-1
        print new_index
        new_array[new_index] = name
        bucket[c] -=1
    print new_array

str = ["Bill","Bob ","Art","Candy","Andy"]
sort(str)
