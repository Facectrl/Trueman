a, b, c = int(input(':')), int(input(':')), int(input(':'))
if a > 0 < c and b > 0:
    print(a + c + b)
if a < 0 < c and b > 0:
    print(c + b)
if c < 0 < a and b > 0:
    print(a + b)
if b < 0 < c and a > 0:
    print(a + c)
if b < 0 < a and c < 0:
    print(0)
if a < 0 > b and c > 0:
    print(c)
if a > 0 < b and c < 0:
    print(a)
if a < 0 < b and c < 0:
    print(b)

##
a, b, c = int(input(':')), int(input(':')), int(input(':'))
counter = 0
if a > 0:
    counter += + a
if b > 0:
    counter += + b
if c > 0:
    counter += + c
print(counter)