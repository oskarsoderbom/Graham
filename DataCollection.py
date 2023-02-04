import yfinance


listofomxcomps = ['ERIC-B.ST','SCA-B.ST','HM-B.ST','ATCO-A.ST','ATCO-B.ST','INVE-B.ST',
'SAND.ST','SWED-A.ST','NDA-SE.ST','SEB-A.ST','BOL.ST','SKF-B.ST','SINCH.ST','ESSITY-B.ST',
'ALIV-SDB.ST','ELUX-B.ST','ALFA.ST','VOLV-B.ST','HEXA-B.ST','TEL2-B.ST','ABB.ST','AZN.ST',
'EVO.ST','GETI-B.ST','SBB-B.ST','SHB-A.ST','TELIA.ST','KINV-B.ST','ASSA-B.ST']

onecomplist = ['ERIC-B.ST']
for com in onecomplist:

    comp = yfinance.Ticker(com)

    print('Historic Dividends')
    print(comp)

    print(comp.dividends)
    
    print('CashFlow')
    print(comp)
    print(comp.cash_flow)
    print('Income Statement')
    print(comp)
    print(comp.income_stmt)
    print('Balance Sheet')
    print(comp)
    print(comp.balance_sheet)