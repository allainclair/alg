# date: 2012-04-16 (16apr2012)
# the 'quicksort' and a 'median' algorithm that use a 'partition' algorithm to solve these problems.
# created by Allainclair Flausino dos Santos
# contact: allainclair@gmail.com
 
def partition(A, p, r):
    """
   >>> A = [1, 4, 4, 5, 7, 15, 8, 3, 10, 2, 9, 7]
   >>> partition(A, 0, 11)
   7
   >>> print A
   [1, 4, 4, 5, 7, 3, 2, 7, 10, 8, 9, 15]
   """
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i] # switch elements
    A[i+1], A[r] = A[r], A[i+1]
    return i+1
 
def median(A, p, r):
    """
   >>> A = [1, 4, 4, 5, 7, 15, 8, 3, 10, 2, 9, 7]
   >>> median(A, 0, 11)
   6
   """
    mid = (p+r)/2 +1
    q = partition(A, p, r)
    while q != mid:
        if q > mid:
            q = partition(A, p, q - 1)
        elif q < mid:
            q = partition(A, q + 1, r)
    return q # median index
 
def quicksort(A, p, r):
    """
   >>> A = [1, 4, 4, 5, 7, 15, 8, 3, 10, 2, 9, 7]
   >>> quicksort(A, 0, 11)
   >>> A
   [1, 2, 3, 4, 4, 5, 7, 7, 8, 9, 10, 15]
   """
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)
