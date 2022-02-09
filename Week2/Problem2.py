amount = 0
initial = 0
interest = 7
years = 40
i = 1
while i < years:
    initial += 6000
    i += 1
    amount = initial * (1 + (interest/100))** i
    initial = amount
nice = "{:,.2f}".format(amount)
print (nice)
