rub = int(input("Enter the amount of rubles: "))
dollar_exchange_rate = float(input("Enter the dollar to ruble exchange rate: "))
commission = int(input("Enter the commission percentage: ")) / 100

bucks = rub / dollar_exchange_rate

print(round(bucks - (bucks*commission), 2))

#    Multiple Input Handling
#    Complex Arithmetic Expressions
#    Algorithmic Logic
#    Structured Output