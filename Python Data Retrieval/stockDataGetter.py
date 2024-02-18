import pandas as pd
import yfinance as yf

def retrieve_stock_data(symbols, start_date, end_date):
    for symbol in symbols:
        data = yf.download(symbol, start=start_date, end=end_date)
        filename = f"Stock_Data\{symbol}.csv"
        data.to_csv(filename)

def save_to_csv(data, filename):
    data.to_csv(filename)

# Example usage
symbols = ['SPY', 'QQQ', 'IWM', 'DIA', 'GLD', 'SLV', 'AAPL', 'LHX', 'KEY', 'KRE', 'AMZN', 'GOOG', 'META', 'DXCM', 'TSLA', 'NVDA', 'MSFT', 'JPM', 'BAC', 'WFC', 'C', 'V', 'MA', 'PYPL', 'ADBE', 'CRM', 'NFLX', 'DIS', 'HD', 'MCD', 'NKE', 'SBUX', 'KO', 'PEP', 'PG', 'JNJ', 'UNH', 'PFE', 'MRK', 'ABBV', 'CVS', 'WMT', 'TGT', 'COST', 'LOW', 'TJX', 'M', 'AMT', 'CCI', 'PLD', 'SPG', 'EQIX', 'DLR', 'ARM', 'PSA', 'AVB', 'EQR', 'AIV', 'UDR', 'VTR', 'O', 'WY', 'BXP', 'SLG', 'ARE', 'HST', 'HLT', 'MAR', 'H',  'IHG', 'CCL', 'RCL', 'NCLH', 'LUV', 'UAL', 'DAL', 'AAL', 'ALK', 'EXPE', 'BKNG', 'TRIP', 'SIX', 'FUN', 'PLNT', 'SEAS', 'MGM', 'WYNN', 'LVS', 'ROST', 'BBY', 'TSCO', 'DG', 'DLTR', 'KR', 'SOXL', 'TQQQ', 'FNGU', 'SPXL', 'UDOW', 'TNA', 'NUGT', 'JNUG', 'ERX', 'FAS', 'TLT', 'XLE', 'XLF', 'XLU', 'XLK', 'XLI', 'XLB', 'XLP', 'XLV', 'XLY', 'XBI', 'XRT', 'XHB', 'XME', 'XSD', 'XSW', 'XITK', 'XNTK', 'XWEB', 'BOIL', 'USO', 'AMD', 'INTC', 'MU', 'QCOM', 'TXN', 'AVGO', 'AMAT', 'ADP', 'ADSK', 'ASML', 'BIDU', 'BIIB', 'CDNS', 'CHKP', 'COIN', 'EA', 'EBAY', 'FAST', 'GILD', 'HAS', 'HSIC', 'IDXX', 'ILMN', 'INCY', 'INTU', 'ISRG', 'JBHT', 'KLAC', 'LRCX', 'MCHP', 'MDLZ', 'MNST', 'NTAP', 'NTES', 'XOM', 'CVX', 'GS', 'UNP', 'RTX', 'BA', 'MMM', 'CAT', 'IBM', 'HON', 'VZ', 'LMT', 'GE', 'LLY', 'SMCI', 'SCHW', 'GDX',  'EWZ', 'LIN', 'CSCO', 'DHR', 'UPS', 'BX', 'TMO', 'AMGN', 'MDT', 'BLK', 'PM', 'PNC', 'UBER', 'ABNB', 'NIO', 'TSM', 'SQ', 'ZM', 'DOCU', 'CRWD', 'NET', 'ZS', 'OKTA', 'MDB', 'DDOG', 'SNOW', 'FSLY', 'TWLO', 'ETSY', 'BRK-B', 'GOOGL', 'ACN', 'ABT', 'TMUS', 'COP', 'MS', 'BMY', 'NOW', 'SPGI', 'AXP', 'DE', 'TM', 'ELV', 'NEE', 'SYK', 'MMC', 'VRTX', 'PGR', 'CI', 'REGN', 'CB', 'SLB', 'ADI', 'ETN', 'CME', 'PANW', 'ZTS', 'MO', 'BDX', 'NOC', 'BSX', 'SNPS', 'SO', 'FI', 'WM', 'LULU', 'FDX', 'MSI', 'KHC', 'PLTR',  'TTWO', 'HYG', 'IVV', 'LQD', 'IEF',  'ARKK', 'SOXX', 'QUAL', 'XLRE', 'MSTR', 'HIBL', 'OILU', 'KOLD', 'ARKG', 'ARKF', 'ARKW', 'SPXU', 'TZA', 'DUST', 'SPXS', 'SDOW', 'TMF', 'TECL', 'LABD', 'DPST', 'NAIL', 'TMV',  'FAZ',  'DRV', 'WFH', 'MIDU', 'BRZU', 'CURE', 'UTSL',  'EDZ',  'SPUU', 'DRN', 'RETL', 'FNGG', 'TYD', 'KORU', 'INDL', 'MEXX', 'EURL', 'CLDL', 'WANT', 'WEBL', 'DFEN',  'UBOT', 'ZSL', 'UGL', 'AGQ', 'BITO', 'UCO', 'SCO',  'PENN', 'SOFI', 'EFA', 'AFRM',  'MARA', 'PDD', 'MELI', 'ANET', 'KWEB', 'T', 'FIVE', 'JWN', 'PSX', 'ITW', 'CCJ','ALLE', 'SPOT', 'XYL', 'SNAP', 'ROKU', 'UPST', 'MARA', 'CLSK', 'CURE']
start_date = '2020-01-01'
end_date = '2024-02-16'

retrieve_stock_data(symbols, start_date, end_date)
