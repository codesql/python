from googlefinance import getQuotes
#import json
#print json.dumps(getQuotes('VMW'), indent=2)
#print getQuotes('MSFT')
x = ('VMW', 'MSFT', 'STK', 'ORCL', 'WDC','haha', 'APPL', 'VMEM','HPE')
#print "Index        Symbol       Current Price      Last Traded Price     Last Traded Time"
print "{:<20} {:<20} {:<20} {:<20} {:<20}".format('Index','Symbol','Current Price', 'Last Traded Price', 'Last Traded Time')
print "_____________________________________________________________________________________________________________"
count = 0
for row in getQuotes(x):
    count = count + 1
    print count, "-", row['StockSymbol'].ljust(20), row['Index'].ljust(20), row['LastTradeWithCurrency'].ljust(20), row['LastTradeTime'].ljust(20), row['LastTradePrice'].ljust(20)
