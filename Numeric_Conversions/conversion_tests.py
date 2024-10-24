# Description: This script tests various numeric
# conversion techniques
# Author: Sam Q. Newprogrammer

a = " 101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5 '

# ai = int(a.strip())
# ValueError: invalid literal for int() with base 10: '101.1'
af = float(a.strip())
ai = int(af)

bi = int(b)
bf = float(b)

# ci = int(c)
# ValueError: invalid literal for int() with base 10: '402 Stevens'

# cf = float(c)
#ValueError: could not convert string to float: '402 Stevens'

cn = c[:3]  
ci = int(cn) 

# di = int(d)
# ValueError: invalid literal for int() with base 10: 'Number 5 '

# df = float(d)
# ValueError: invalid literal for int() with base 10: 'Number 5 '

dn = d[-2]  
di = int(dn)  



print(f"a (as float): {af}, type: {type(af)}")
print(f"a (as int): {ai}, type: {type(ai)}")

print(f"b (as int): {bi}, type: {type(bi)}")
print(f"b (as float): {bf}, type: {type(bf)}")

print(f"c (numeric portion as int): {ci}, type: {type(ci)}")

print(f"d (numeric portion as int): {di}, type: {type(di)}")
