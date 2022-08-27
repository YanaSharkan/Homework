from decimal import Decimal

uah_amount = Decimal(input('Enter the amount of hryvnias (UAH): '))
rate = Decimal(40.89)
usd_amount = uah_amount / rate

print('As of August 26, 2022, it is {:.2f} USD'.format(usd_amount))