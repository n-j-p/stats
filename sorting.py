def qsort0(X=[5,14,2,3,9,10,6,1,4,7,13]): # a list
    '''Recursive implementation of quicksort'''
    def qsort0_rec(X,L,R):
        if (R > L):
            pivot = X[R] # Just choose the right-most element of X as pivot
            Xp,i = _partition(X[L:R], pivot)#This implementation uses sentinels
            X[L:(R+1)] = Xp
            X = qsort0_rec(X,L,L+i-1)
            X = qsort0_rec(X,L+i+1,R)
        return X    
    N = len(X)
    Y = list(X) # copy X
    Y = qsort0_rec(Y,0,N-1)
    return Y

def _partition(X, pivot):
    '''partition the list X according to the pivot, i.e.
    result is a list of length len(X)+1, with pivot element in correct (sorted)
    place, everything to the left of pivot less than or equal to the pivot 
    element, and everything to the right of pivot greater than or equal to the
    pivot element.

    Initial implementation uses sentinels (+/- numpy's inf).'''
    from numpy import inf
    n = len(X)
    if n > 0:
        X.insert(0,-inf)
        X.append(inf)
        i = 0
        j = n+1
        while True:
            i += 1
            while X[i] < pivot:
                i += 1
            j -= 1
            while X[j] > pivot:
                j -= 1
            if i >= j:
                break
            X[j],X[i]=X[i],X[j]
        X.pop()
        if i != n + 1:
            X.append(X[i])
            X[i] = pivot
        else:
            X.append(pivot)
        return X[1:], i-1
    else:
        return [pivot], 0


def sort3(abc):
    '''sort a list or tuple of three items'''
    abc = list(abc)
    if abc[0] > abc[1]:
        abc[0], abc[1] = abc[1], abc[0]
    if abc[0] > abc[2]:
        abc[0], abc[2] = abc[2], abc[0]
    if abc[1] > abc[2]:
        abc[1], abc[2] = abc[2], abc[1]
    return abc

def isort(alist):
    '''insertion sort'''
    x = list(alist)
    n = len(x)
    i = 1
    while True:
        if x[i] >= x[i-1]:
            i += 1
            if i == n:
                return x
        j = i - 1
        while x[i] < x[j]:
            j -= 1
            if j == -1:
                break
        pdb.set_trace()
        j += 1
        if j < i:
            x.insert(j, x.pop(i))
