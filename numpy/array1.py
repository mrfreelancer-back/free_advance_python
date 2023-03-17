import numpy as nmp
from numpy import array as arr
from numpy import eye as ey
from numpy import identity as dntt
from numpy import ones as ons
from numpy import zeros as zrs
from numpy import full as fl
from numpy import full_like as fllk

i = ([1, 2, 3], [4, 5, 6])
s = (['1', '2', '3'], ['4', '5', '6'])
f = ([1., 2., 3.], [4., 5., 6.])
b = ([True, False], [False, True])

a_nmp = arr([i])
print(a_nmp)

m = arr(nmp.mat('1 2 3; 4 5 6'))
print(m)

eye_arr = ey(2, 5, k=3)
eye_arr2 = ey(4, 5, k=1)
print(eye_arr)
print(eye_arr2)

int_id_arr = dntt(3, dtype=int)
float_id_arr = dntt(3, dtype=float)
str_id_arr = dntt(3, dtype=str)
bool_id_arr = dntt(3, dtype=bool)
print(int_id_arr)
print(float_id_arr)
print(str_id_arr)
print(bool_id_arr)

ones_int = ons([3, 3], dtype=int)
ones_bool = ons([3, 3], dtype=bool)
print(ones_int)
print(ones_bool)

zeros_float = zrs([4, 4], dtype=float)
zeros_str = zrs([4, 4], dtype=str)
print(zeros_float)
print(zeros_str)

full_arr = fl([5, 5], 128)
full_arr2 = fl([5, 5], 'ali')
print(full_arr)
print(full_arr2)

full_like_int = fllk(i, 4)
full_like_float = fllk(f, 4)
full_like_str = fllk(s, 4)
full_like_bool = fllk(b, 0)
full_like_bool2 = fllk(b, 1)

print(full_like_int)
print(full_like_float)
print(full_like_str)
print(full_like_bool)
print(full_like_bool2)