import csv
import yfinance as yf
import datetime

def extract_data(filename):
  """
  Extracts symbol and buy time from each row of a CSV file.

  Args:
      filename: Path to the CSV file.

  Returns:
      A list of dictionaries, where each dictionary contains the symbol and buy time for a row.
  """
  data = []
  with open(filename, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader)  # Skip the header row

    for row in reader:
      symbol = row[1].strip()
      buy_time = row[3].strip()  # Adjust index based on actual buy time column
      data.append({'symbol': symbol, 'buy_time': buy_time})

  return data

# Example usage
data = extract_data('topSucessRateTrades.csv')
#reverse the list
data = data[::-1]


positiveTrades = 0
negativeTrades = 0
total_return = 0

for entry in data:
    print(f"Symbol: {entry['symbol']}, Buy Time: {entry['buy_time']}")
    stock = yf.Ticker(entry['symbol'])
    buy_date = entry['buy_time'].split(' ')[0]
    try:
        buy_price = (stock.history(start=buy_date)['Close'][0])
    except IndexError:
        print(f"No data found for {entry['symbol']}, skipping trade")
        continue
    
    sell_date = buy_date
    while True:
        print(f"Checking price for {entry['symbol']} on {sell_date}")
        try:
            sell_price = (stock.history(start=sell_date)['Close'][0])
        except IndexError:
            print(f"No data found for {entry['symbol']} on {sell_date}, skipping trade")
            break
        
        if sell_price > buy_price:
            profit = sell_price - buy_price
            print(f"Buy price: {buy_price}, Sell price: {sell_price}, Profit: {profit}")
            total_return += profit
            positiveTrades += 1
            break
        elif sell_price < buy_price * 0.94:
            loss = sell_price - buy_price
            print(f"Buy price: {buy_price}, Sell price: {sell_price}, Loss: {loss}")
            total_return += loss
            negativeTrades += 1
            break
        else:
            # Increment date by 1 day
            sell_date = datetime.datetime.strptime(sell_date, '%Y-%m-%d')
            sell_date += datetime.timedelta(days=1)
            sell_date = sell_date.strftime('%Y-%m-%d')
            continue

print(f"Positive trades: {positiveTrades}, Negative trades: {negativeTrades}")
percent = (positiveTrades / (positiveTrades + negativeTrades)) * 100
print(f"Percent of positive trades: {percent}%")

total_percentage_return = (total_return / 1000) * 100
print(f"Total percentage return: {total_percentage_return}%")


