from yaml import load_all as ld_al
from yaml import FullLoader as fll
from yaml import safe_load_all as sf_ld

with open('D:\\free_advance_python\\python_files\\yaml\\my_yaml.yml') as stream:
    for i in ld_al(stream, Loader=fll):
        print(i, type(i))
# both are the same! recomended to use the safe one        
with open('D:\\free_advance_python\\python_files\\yaml\\my_yaml.yml') as stream2:
    for each in sf_ld(stream2):
        print(each, type(each))