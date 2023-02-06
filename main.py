from GrahamClass import Stock

omxstocks = ['ERIC-B.ST','SCA-B.ST','HM-B.ST','ATCO-A.ST','ATCO-B.ST',
'SAND.ST','SWED-A.ST','NDA-SE.ST','SEB-A.ST','BOL.ST','SKF-B.ST','SINCH.ST','ESSITY-B.ST',
'ALIV-SDB.ST','ELUX-B.ST','ALFA.ST','VOLV-B.ST','HEXA-B.ST','TEL2-B.ST','ABB.ST','AZN.ST',
'EVO.ST','GETI-B.ST','SBB-B.ST','SHB-A.ST','TELIA.ST','KINV-B.ST','ASSA-B.ST']

eligible = []
for company in omxstocks:
    comp = Stock(company)
    #comp.check_current_ratio()
    comp.check_price_earnings()
    comp.check_price_to_asset()
    comp.div_years_check()
    comp.market_cap_check()

    print(company)
    print(comp.score)
    if comp.score >= 4:
        eligible.append(company)
    else:
        print('not sufficient')