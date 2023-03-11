from csv import reader as rdr
from csv import writer as rtr

employees_inf = list()

with open('./mycsv.csv') as csv_file:
    csv_reader = rdr(csv_file, delimiter=',')
    line_counter = 0
    
    for row in csv_reader:
        if line_counter == 0:
            print(f"Column titles are {','.join(row)}")
            line_counter += 1
        else:
            print(f'{row[0]} works in {row[1]} department in {row[3]} city at {row[2]}')
            employees_inf.append(row)
            line_counter += 1
            
    print(f'{line_counter} lines processed')

with open('./output.csv', 'x') as out_csv:
    csv_writer = rtr(out_csv)
    
    for each in employees_inf:
        csv_writer.writerow(each)
        
    print(f'{len(employees_inf)} employees\'s information added')