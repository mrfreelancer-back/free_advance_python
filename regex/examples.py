from re import findall, finditer

text = "I am Alyi & please pay attention carefully"

res = findall(r"\w+ly\b" ,text)
print(res)

# similar code in string functions:
print([word for word in text.split() if word.endswith('ly')])

for mtch in finditer(r'\w+ly\b', text): # returns the match objects: start(), end(), group()
    print('%02d-%02d: %s' %(mtch.start(), mtch.end(), mtch.group(0)))