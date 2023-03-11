from yaml import safe_load_all as sf_ld

with open('D:\\free_advance_python\\python_files\\yaml\\person.yaml') as yml_file:
    
    for i in sf_ld(yml_file):
        print(i, type(i))
        print(i['person'], type(i))
        print(i['person']['friends'], type(i))
        print(i['person']['friends'][0], type(i))