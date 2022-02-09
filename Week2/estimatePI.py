a = 1
b = 1/(2**(1/2))
t = 1/4
p = 1
i = 1
while i <= 10:
    an = (a + b)/2
    bn = (a*b)**(1/2)
    tn = t - p * ((a - an)**2)
    pn = 2*p
    pie = ((an + bn)**2)/(4*tn)
    a = an
    b = bn
    p = pn
    t = tn
    i+=1
    print(pie)