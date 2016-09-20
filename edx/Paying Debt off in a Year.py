balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

for i in range (1,13):
    monthlyInterestRate = annualInterestRate / 12.0
    minimumMonthlyPayment = monthlyPaymentRate * balance
    monthlyUnpaidBalance = balance - minimumMonthlyPayment
    balance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)

print ("Remaining Balance: %s" % round(balance,2))