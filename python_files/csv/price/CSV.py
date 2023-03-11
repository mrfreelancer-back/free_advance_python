from csv import reader as rdr
from csv import writer as rtr

prices_d = dict()
with open('D:\\free_advance_python\\python_files\\price\\prices.csv') as prices:
    
    reader = rdr(prices)
    c = 0
    
    for row in reader:
        if c == 0:
            print(f'prices.csv first row {row}')
            c += 1
        else:
            (item, price) = row
            prices_d[item] = price
            
withdraws = list()
all_buys = dict()

with open('D:\\free_advance_python\\python_files\\price\\buys.csv') as buys:
    
    reader = rdr(buys)
    c = 0
    
    for row in reader:
        if c == 0:
            print(f'buys.csv first row {row}')
            c += 1
        else:
            if row[1] in list(prices_d.keys()):
                prc = int(row[2]) * int(prices_d[row[1]])
                withdraws.append([row[0], prc])
                
    for each in withdraws:
        if each[0] not in list(all_buys.keys()):
            all_buys[each[0]] = each[1]
        else:
            all_buys[each[0]] += each[1]
    
with open('D:\\free_advance_python\\python_files\\price\\output.csv', 'x') as output:
    writer = rtr(output)
    
    for person in all_buys:
        writer.writerow([person, all_buys[person]])