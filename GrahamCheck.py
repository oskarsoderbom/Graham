import RuleChecking

listofomxcomps = ['ERIC-B.ST','SCA-B.ST','HM-B.ST','ATCO-A.ST','ATCO-B.ST','INVE-B.ST',
'SAND.ST','SWED-A.ST','NDA-SE.ST','SEB-A.ST','BOL.ST','SKF-B.ST','SINCH.ST','ESSITY-B.ST',
'ALIV-SDB.ST','ELUX-B.ST','ALFA.ST','VOLV-B.ST','HEXA-B.ST','TEL2-B.ST','ABB.ST','AZN.ST',
'EVO.ST','GETI-B.ST','SBB-B.ST','SHB-A.ST','TELIA.ST','KINV-B.ST','ASSA-B.ST']

onecomplist = ['ERIC-B.ST']
for com in listofomxcomps:
    print(com)
    RuleChecking.check_current_ratio(com)
    RuleChecking.check_price_earnings(com)
    RuleChecking.check_price_to_asset(com)
    RuleChecking.market_cap_check(com)
    RuleChecking.div_years_check(com)