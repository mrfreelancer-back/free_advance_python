from re import findall as fndll
from re import split as splt
from re import sub as sb
from re import search as srch
from re import match as mtch

# findall()
fnd_string = "Hello i'm Barkhordar"
fnd_pettern = "\d+"

fnd_result = fndll(fnd_pettern, fnd_string)
print(fnd_result) # output -> [] : no digits available

# split()
splt_string = "Hello i'm Barkhordar at 234 st in 120988 avenue"
splt_pettern = "\d+"

splt_result = splt(splt_pettern, splt_string)
print(splt_result)

# sub() replaces in the string
sb_string = "Hello i'm Ali Barkhordar"
sb_pattern = "\s+"
replace = " - "

sb_result = sb(sb_pattern, replace, sb_string)
print(sb_result)

# search()
srch_string = "Hello i'm Ali Barkhordar 20"
srch_pattern = "\d+"

srch_result = srch(srch_pattern, srch_string)

if srch_result:
    print("Search successfully")
else:
    print("No")

# match()
mtch_string = "Hello i'm Ali Barkhordar 20"
mtch_pattern = "\d+"

mtch_result = mtch(mtch_pattern, mtch_string)

if mtch_result:
    print("Matched")
else:
    print("No") # output -> No : the digit must in the start of the string
