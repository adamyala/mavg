import ystockquote

data = ystockquote.get_historical_prices('GOOG','2013-08-21','2014-08-21')

print len(data)

print data['2013-08-21']