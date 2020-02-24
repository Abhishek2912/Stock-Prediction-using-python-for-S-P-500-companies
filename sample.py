import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
from matplotlib import style
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates 
import pandas_datareader.data as web

style.use('ggplot')
start = dt.datetime(2000,1,1)
end=dt.datetime(2016,12,31)

df=web.DataReader('BF-B','yahoo',start,end)

df.to_csv('BF.B.csv')
