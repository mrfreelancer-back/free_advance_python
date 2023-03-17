import time
from numpy import arange as arng

vector_size = 1000000

def list_view():
    tm = time.time()
    lst1 = range(vector_size)
    lst2 = range(vector_size)
    summation = [lst1[i] + lst2[i] for i in range(len(lst1))]
    return time.time() - tm

def numpy_view():
    tm = time.time()
    nmp1 = arng(vector_size)
    nmp2 = arng(vector_size)
    summation = nmp1 + nmp2
    return time.time() - tm

numpy = numpy_view()
lst = list_view()

print(lst/numpy)