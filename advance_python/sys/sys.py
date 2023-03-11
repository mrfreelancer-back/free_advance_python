import sys as s 

print(s.argv)
print(f'The path is {s.argv[0]}')
print(f'My python is in {s.base_exec_prefix}')
for inf in s.path:
    print(f'python installation informations path: {inf}')