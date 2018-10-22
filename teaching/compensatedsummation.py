numbers = [1.0e+16, 1.0, 1.0, 1.0, 1.0]
sum = 0.0
c = 0.0
for a in numbers:
    y = a - c
    t = sum + y
    c = (t-sum) - y
    sum = t
    print "%.20f" % sum

