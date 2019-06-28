import datetime
import pandas_datareader.data as data

start = datetime.datetime(2012, 1, 1)
end = datetime.datetime(2012, 12, 30)
msft = data.DataReader("MSFT", 'yahoo', start, end)
aapl = data.DataReader("AAPL", 'yahoo', start, end)

print(type(msft))
print(msft[:3])
print(msft.head())
print(msft.tail())


# print(type(aapl))
# print(aapl)
#
# msft.to_csv("msft.csv")
# aapl.to_csv("aapl.csv")