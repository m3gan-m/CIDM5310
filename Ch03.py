print("Chapter 3 Exercises")
print("-------------------")
print()

print("1.")
faang = pd.DataFrame()
for ticker in ['fb', 'aapl', 'amzn', 'nflx', 'goog']:
    df = pd.read_csv(f'/data/{ticker}.csv')
    df.insert(0, 'ticker', ticker.upper())
    faang = faang.append(df)
faang.to_csv('faang.csv', index=False)
print()

print("2.")
faang = faang.assign(
    date=lambda x: pd.to_datetime(x.date),
    volume=lambda x: x.volume.astype(int)
).sort_values(
    ['date', 'ticker']
)
faang.head()
print()

print("3.",faang.nsmallest(7, 'volume'))
print()

print("4.")
melted_faang = faang.melt(
    id_vars=['ticker', 'date'], 
    value_vars=['open', 'high', 'low', 'close', 'volume']
)
melted_faang.head()
print()

print("5. Since this data set is quite big, the date could be dropped and interpolate that way.")
print("Only down side is interpolating may hide any sharp swings")
print()

print("6.")
covid = pd.read_csv('/data/covid19_cases.csv').assign(
    date=lambda x: pd.to_datetime(x.dateRep, format='%d/%m/%Y')
).set_index('date').replace(
    'United_States_of_America', 'USA'
).replace('United_Kingdom', 'UK').sort_index()
covid[
    covid.countriesAndTerritories.isin([
        'Argentina', 'Brazil', 'China', 'Colombia', 'India', 'Italy', 
        'Mexico', 'Peru', 'Russia', 'Spain', 'Turkey', 'UK', 'USA'
    ])
].reset_index().pivot(index='date', columns='countriesAndTerritories', values='cases').fillna(0)
print()

print("7.")
pd.read_csv('/data/covid19_total_cases.csv', index_col='index')\
    .T.nlargest(20, 'cases').sort_values('cases', ascending=False)
print()