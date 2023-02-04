import GrahamRules
import pandas as pd 

def div_years_check(divident_data: pd.Series):
    '''Checking rule nr X for years of divindends'''
    divident_df = pd.DataFrame(divident_data.index)
    divident_df['Years'] = divident_df['Date'].dt.year
    
    if len(divident_df['Years'].unique()) >= GrahamRules.DIVIDENT_PAYMENT_YEARS:
        print(f"dividends history ok, years = {len(divident_df['Years'].unique())}, last year = {divident_df['Years'].max()}")
    else:
        print('dividens history too short')

