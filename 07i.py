def count11(seq):
    n = 0
    for i in range(len(seq)-1):
        if (seq[i] == 1 & seq[i+1] == 1):
            n += 1
    return n

print(count11([0, 0, 1, 1, 1, 0])) # this should print 2
