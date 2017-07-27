# https://www.reddit.com/r/beginnerprojects/comments/19jkn8/project_change_calculator/

import os

while 1 == 1:
	
	given = input("How much money was given?\n")
	price = input("Price of the item?\n")

	change = given - price

	q = change // 0.25
	qValue = change - (q * 0.25)
	d = (change - qValue) // 0.10
	dValue = qValue - (d * 0.10)
	n = (change - dValue) // 0.05
	nValue = dValue - (n * 0.05)
	p = (change - nValue) // 0.01

	print(" %s Quarters\n %s Dime\n %s Nickels\n %s Pennies\n" % (q, d, n, p))

	raw_input("Press enter to restart calculator")

	os.system('cls')