import os as o

print(o.name)
print(o.getcwd())
o.chdir(r'../..')
o.rmdir('os-modules100')
o.mkdir('os-modules1000')
print(o.getcwd())
