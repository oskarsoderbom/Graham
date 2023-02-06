import yfinance
import pandas as pd 
import GrahamRules

class Stock:
    '''Class for stocks, with methods for calculating some variables and checking against Grahams rules'''

    def __init__(self, ticker) -> None:
        self.ticker = yfinance.Ticker(ticker)
        self.score = 0
        

    def check_current_ratio(self):
        ''' Checking rule nr 2'''
        bs = self.ticker.get_balance_sheet()
        latestyear = max(bs.columns)
        currentasset = bs[latestyear]['CurrentAssets']
        current_liabilities = bs[latestyear]['CurrentLiabilities']
        current_ratio = currentasset / current_liabilities
        
        if current_ratio > GrahamRules.CURRENT_RATIO_CEILING:
            print(f"The Current Ratio is {current_ratio} to high")
        elif current_ratio < GrahamRules.CURRENT_RATIO_FLOOR:
            print(f"The Current Ratio is {current_ratio} to low")
        else:
            print(f"The current ratio is within the bounds: {current_ratio}")
            self.score += 1


    def div_years_check(self):
        '''Checking rule nr 4 for years of divindends'''

        divident_data = self.ticker.dividends
        divident_df = pd.DataFrame(divident_data.index)
        divident_df['Years'] = divident_df['Date'].dt.year
        
        if len(divident_df['Years'].unique()) >= GrahamRules.DIVIDENT_PAYMENT_YEARS:
            print(f"dividends history ok, years = {len(divident_df['Years'].unique())}, last year = {divident_df['Years'].max()}")
            self.score += 1
        else:
            print('dividens history too short')

    def market_cap_check(self):
        ''' check nr 1
        need to add basecurrency, for now just use SEK(?)'''

        if self.ticker.fast_info.market_cap > GrahamRules.MARKETCAP_FLOOR:
            print('Sufficient Market Cap')
            self.score += 1
        else:
            print('Too small')

    def check_price_earnings(self):
        '''Checking rule no 6 - using trailing PE'''
        statistics = self.ticker.stats()
        pe = statistics['summaryDetail']['trailingPE']

        if pe < GrahamRules.PE_CEILING:
            print(f'PE is {pe} and below the PE Ceiling')
            self.score += 1
        else:
            print(f'PE is {pe} and above the PE Ceiling')

    def check_price_to_asset(self):
        ''' Checking rule no 7 but using price to book instead'''

        statistics = self.ticker.stats()

        if statistics['defaultKeyStatistics']['priceToBook'] < GrahamRules.PRICE_ASSET_CEILING:
            print(f"Price to Book is {statistics['defaultKeyStatistics']['priceToBook']} which is below the ceiling")
            self.score += 1
        else:
            print(f"Price to Book is {statistics['defaultKeyStatistics']['priceToBook']} which is above the ceiling")

