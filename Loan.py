# Get Details of Loan
money_owed = float(input (' How much do you owe, in dollars?\n')) # $50,000
apr = float (input('what is the annual percentage rate of the loan \n')) # 3%
payment = float (input('How will you pay off each month in dollars?\n')) #$1,000
months = int(input('How many months.  do you want to see the results for?\n')) # 24 

monthly_rate = apr/100/12

for i in range(months): 
    # Calculate interest to pay
    interest_paid = money_owed*monthly_rate
    
    #Add in interest
    money_owed = money_owed + interest_paid

    # Make Payment 
    money_owed = money_owed - payment 

print('Paid', payment, 'of which', interest_paid, 'was interest', end= ' ')
print('Now I owe', money_owed)