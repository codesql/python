from googlefinance import getQuotes

import sqlite3 as lite
import sys

try:
    conn = lite.connect('test.db')
    print "Connected to database successfully"

    x = ('VMW', 'MSFT', 'STK', 'ORCL', 'WDC','haha', 'AAPL', 'VMEM','HPE','DGL')
    bought_price = ('60', '30', '20', '35', '112', '1', '54', '65', '20', '21')
    c = conn.cursor()

    #clena up tables
    c.executescript(
    '''
    drop table if exists stocks;
    drop table if exists prices;
    drop view if exists stock_overview;
    '''
    )

    #create stock table. Create primary key for joining later on.
    c.execute(
    '''create table if not exists stocks
    (
     id integer primary key autoincrement,
     stocksymbol text null ,
     index_col text null,
     lasttradewithcurrency text null,
     lasttradetime text null,
     lasttradeprice text null );
     ''')

    #create price table
    c.execute(
    '''
    create table if not exists prices
    (
    id integer primary key autoincrement,
    bought_price text not null);
    ''')

    #create stock_overview view
    c.execute(
    '''
     create view if not exists stock_overview as select s.id, s.stocksymbol, s.index_col, s.lasttradewithcurrency, s.lasttradetime, s.lasttradeprice, p.bought_price from stocks s, prices p where s.id = p.id;
    ''')

    #print "Table and views created correctly"

    #c.execute("insert into stocks (stocksymbol, index_col, lasttradewithcurrency, lasttradetime, lasttradeprice, bought_price) values (row['StockSymbol'],row['Index'], row['LastTradeWithCurrency'],row['LastTradeTime'], row['LastTradePrice'],0 ) ");
    #row['StockSymbol'].ljust(20), row['Index'].ljust(20), row['LastTradeWithCurrency'].ljust(20), row['LastTradeTime'].ljust(20), row['LastTradePrice'].ljust(20)
    '''
    for row in getQuotes(x):
         print row['StockSymbol'].ljust(20), row['Index'].ljust(20), row['LastTradeWithCurrency'].ljust(20), row['LastTradeTime'].ljust(20), row['LastTradePrice'].ljust(20)
        conn.execute ("insert into stocks (stocksymbol, index_col, lasttradewithcurrency, lasttradetime, lasttradeprice, bought_price) values ('h','h','n','m','d','t') ");

    conn.commit()
    '''

    #insert data into bought_price table
    for row_price in bought_price:
         bp = row_price;
    #    print "BBBBBBBBBBBBBB", bp
         c.execute('''insert into prices (bought_price) values (?) ''', (bp,))
    conn.commit()

    # insert data into stock quotes
    for row in getQuotes(x):
        ss = row['StockSymbol'];
        ind = row['Index'];
        ltc = row['LastTradeWithCurrency'];
        ltt = row['LastTradeTime'];
        ltp = row['LastTradePrice'];
    #    print ss, ind
        c.execute('''INSERT OR IGNORE INTO stocks (stocksymbol,index_col,lasttradewithcurrency,lasttradetime, LastTradePrice ) VALUES (?,?,?,?,? )''', (ss ,ind, ltc, ltt, ltp ) )
    #    c.execute('''insert into stocks (bought_price) values (?) ''', (bp,))
    conn.commit()

    #pulling data from both tables to be presented on stock_overview
    for row1 in c.execute('''select * from stock_overview'''):
            print " ", str(row1[0]).ljust(5, ' '), row1[1].ljust(5, ' '), row1[2].ljust(10, ' '), str(row1[3]).ljust(15, ' '), str(row1[4]).ljust(15, ' '), str(row1[5]).ljust(15, ' '), str(row1[6]).ljust(15, ' '), float(row1[5])-float(row1[6])
except Exception as e:
    conn.rollback()
    raise e
finally:
    conn.close()
