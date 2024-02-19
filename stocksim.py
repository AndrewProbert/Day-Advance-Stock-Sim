from functions import get_stock_price, buy_stock, sell_stock, check_date_valid, print_holdings
import datetime 
import tabulate


start_date = '2022-01-01'
original_balance = 1000
balance = original_balance
holdings = {}
trades = {}  # Separate dictionary to record all trades
x = True

print('Stocksim module loaded'
      ' with start date: ' + start_date)

while x == True:
    
    print (start_date, "Balance:" , balance, "USD", 'Percent Change', balance/original_balance,  end = '\n')
    
    if holdings != {}:
        print_holdings(holdings, start_date)

    while True:
        action = input('What do you want to do? (buy/sell/quit): ')

        if action == 'quit':
            x = False
            break
    
        if action == 'buy':
            ticker = (input('Enter the ticker symbol: ')).upper()
            balance, holdings = buy_stock(ticker, start_date, balance, holdings)
            trades[start_date] = {'action': 'buy', 'ticker': ticker, 'balance': balance}  # Record buy trade
            print('Balance:', balance, 'USD')

        if action == 'sell':
            ticker = input('Enter the ticker symbol: ').upper()
            balance, holdings = sell_stock(ticker, start_date, balance, holdings)
            trades[start_date] = {'action': 'sell', 'ticker': ticker, 'balance': balance}  # Record sell trade

        if action == '1':
            continue

        if action != 'buy' and action != 'sell' and action != 'quit':
            break

    # Increment date by 1 day 
    start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
    start_date += datetime.timedelta(days=1)

    while check_date_valid(start_date) == False:
        print('Checking date:', start_date)
        start_date += datetime.timedelta(days=1)
    
    start_date = start_date.strftime('%Y-%m-%d')

    # Clear the screen
    print('\n'*5)

# Print all trades in tabulate format
print('All trades:')
table_data = []
for date, trade in trades.items():
    table_data.append([date, trade['action'], trade['ticker'], trade['balance']])
print(tabulate(table_data, headers=['Date', 'Action', 'Ticker', 'Balance'], tablefmt='grid'))

#put this in a txt file
with open('trades.txt', 'w') as f:
    f.write(tabulate(table_data, headers=['Date', 'Action', 'Ticker', 'Balance'], tablefmt='grid'))



# Print final balance
print('Final balance:', balance, 'USD')


print('Goodbye!')

