# function to subset coin
def coin_subsetter(coin):
    global analysis # global keyword -->> callable outside function
    crypto_coin = [coin]
    analysis = dataset[dataset.Coin.isin(crypto_coin)]
    print(analysis)
    
# function to append API extracted timestamps to df
def timestamper(dataset):
    n = -100 
    z = 1
    #
    for x in range(len(meta_dataset)):
        n += 100
        z += 100
        #
        dataset.loc[n:z,4] = meta_dataset['API-Request-Timestamp'][x]
        
# Moving Averages
# Simple Moving Average function 
analysis['SMA'] = analysis.iloc[:,1].rolling(window=3).mean() # pandas in-built rolling function -->> simple moving average (SMA)
analysis['CMA_10'] = analysis.iloc[:,4].expanding(min_periods=10).mean() # Cumultive Moving Average function
analysis['EMA'] = analysis.iloc[:,4].ewm(span=40,adjust=False).mean() # Eponential Moving Average

# PCT change function
analysis['rate_pct_change'] = analysis.Rate.pct_change() # percantage value between most recent & present data point
analysis