import yfinance as yf
import tabulate 
from tabulate import tabulate

def get_stock_price(ticker, date):
    stock = yf.Ticker(ticker)
    return stock.history(start=date)['Close'][0]

def buy_stock(ticker, date, balance, holdings):
    price = get_stock_price(ticker, date)
    print('Buying', ticker, 'for', price, 'USD')
    quantity = int(input('How many shares do you want to buy? '))
    cost = price * quantity
    if cost > balance:
        print('Insufficient funds')
        return balance, holdings
    
    else:
        balance -= cost
        holdings[ticker] = {'quantity': quantity, 'buy_price': price, 'buy_date': date}
        return balance, holdings
    
def sell_stock(ticker, date, balance, holdings):
    price = get_stock_price(ticker, date)
    print('Selling', ticker, 'for', price, 'USD')
    quantity = int(input('How many shares do you want to sell? '))
    if quantity > holdings.get(ticker, {}).get('quantity', 0):
        print('Insufficient shares')
        return balance, holdings
    else:
        balance += price * quantity
        holdings[ticker]['quantity'] -= quantity
        if holdings[ticker]['quantity'] == 0:
            del holdings[ticker]
        return balance, holdings
    

def check_date_valid(date):
    #check if there is spy data for the date
    spy = yf.Ticker('SPY')
    spy_data = spy.history(start=date)
    if spy_data.empty:
        return False
    else:
        return True
    
def print_holdings(holdings, date):
    # Print the current holdings in a nice table with percent change and other info
    print('Current holdings:')
    table_data = []
    for ticker, quantity in holdings.items():
        print('Checking price for', ticker)

        price = get_stock_price(ticker, date)
        value = price * quantity['quantity']  # Access quantity correctly
        day_change = price -quantity['buy_price']  # Access buy_price correctly
        percent_change = ((price - quantity['buy_price']) / price) * 100  # Access buy_price correctly
        buy_price = quantity['buy_price']  # Access buy_price correctly
        buy_date = quantity['buy_date']
        cash_return = (price - quantity['buy_price']) * quantity['quantity']
        table_data.append([ticker, quantity['quantity'], price, value, day_change, percent_change, buy_price, buy_date, cash_return])  # Access quantity correctly
    headers = ['Ticker', 'Shares', 'Price', 'Value', 'Day Change', 'Percent Change', 'Buy Price', 'Buy Date', 'Cash Return']
    print(tabulate(table_data, headers=headers, tablefmt='grid'))


