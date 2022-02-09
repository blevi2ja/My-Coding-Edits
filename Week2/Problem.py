year = 10
year2 = 20
year3 = 30
yr10 = 1.75
yr20 = 2.13
yr30 = 2.07 
initial = 1020000000
amount = initial * (1 + (yr10/100))** year
amount2 = initial * (1 + (yr20/100))** year2
amount3 = initial * (1 + (yr30/100))** year3
amount = "{:,.2f}".format(amount)
amount2 = "{:,.2f}".format(amount2)
amount3 = "{:,.2f}".format(amount3)

print('The total amount after ' + str(year) + ' years is $' + str(amount))
print('The total amount after ' + str(year2) + ' years is $' + str(amount2))
print('The total amount after ' + str(year3) + ' years is $' + str(amount3))