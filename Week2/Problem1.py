amount = 0

interest = 7
principle = 0
annuity = 0
a = 0
years = 40
year = 1
i = 0
while i < years:
    principle += 6000
    amount = principle * (1 + (interest/100))** years
    annuity += 1.07**i
    a += 6000 * annuity
    i += 1
amount = a + amount
nice = "{:,.2f}".format(amount)
print (nice)