with open('D:\myfile.txt', 'x') as maker:
    print(type(maker))
    maker.write('Hello World!\nstudent\tBarkhordar')

reader_lines = list()
with open('D:\myfile.txt', 'r') as reader:
    my_list = reader.readlines()
    for each in my_list:
        each = each.rstrip()
        reader_lines.append(each)
for line in reader_lines:
    print(line)