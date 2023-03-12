from re import findall as fnd

text = "Date is 2002-11-27"
text2 = "Today is 2023-04-01"

def date_process(text):
    res = fnd(r'([12]\d{3})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|30[1])', text)
    return res

for each in date_process(text)[0]:
    print(each)
for each in date_process(text2)[0]:
    print(each)
    
def date_print(inpt):
    year, month, day = inpt
    print(f"The date is {year}/{month}/{day}")
    
date_print(date_process(text)[0])
date_print(date_process(text2)[0])