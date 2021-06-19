print("Chapter 4 Exercises")
print("-------------------")
print()

print("1.")
import pandas as pd
import numpy as np
quakes = pd.read_csv('/data/earthquakes.csv')
faang = pd.read_csv('/data/faang.csv', index_col='date', parse_dates=True)
quakes.query(
    "parsed_place == 'Japan' and magType == 'mb' and mag >= 4.9"
)[['mag', 'magType', 'place']]
print(quakes)
print()

print("2.")
quakes.query("magType == 'ml'").assign(
    mag_bin=lambda x: pd.cut(x.mag, np.arange(0, 10))
).mag_bin.value_counts()
print()

print("3.")
faang.groupby('ticker').resample('1M').agg(
    {
        'open': np.mean,
        'high': np.max,
        'low': np.min,
        'close': np.mean,
        'volume': np.sum
    }
)
print()

print("4.")
pd.crosstab(quakes.tsunami, quakes.magType, values=quakes.mag, aggfunc='max')
print()

print("5.")
faang.groupby('ticker').rolling('60D').agg(
    {
        'open': np.mean,
        'high': np.max,
        'low': np.min,
        'close': np.mean,
        'volume': np.sum
    }
)
print()

print("6.")
faang.pivot_table(index='ticker')
print()

print("7.")
faang.loc['2018-Q4'].query("ticker == 'AMZN'").drop(columns='ticker').apply(
    lambda x: x.sub(x.mean()).div(x.std())
).head()
print()

print("8.")
events = pd.DataFrame({
    'ticker': 'FB',
    'date': pd.to_datetime(
         ['2018-07-25', '2018-03-19', '2018-03-20']
    ), 
    'event': [
         'Disappointing user growth announced after close.',
         'Cambridge Analytica story',
         'FTC investigation'
    ]
}).set_index(['date', 'ticker'])

faang.reset_index().set_index(['date', 'ticker']).join(
    events, how='outer'
).sample(10, random_state=0)
print()

print("9.")
faang = faang.reset_index().set_index(['ticker', 'date'])
faang_index = (faang / faang.groupby(level='ticker').transform('first'))
faang_index.groupby(level='ticker').agg('head', 3)
print()

print("10.")
covid = pd.read_csv('../../ch_04/exercises/covid19_cases.csv')\
    .assign(date=lambda x: pd.to_datetime(x.dateRep, format='%d/%m/%Y'))\
    .set_index('date')\
    .replace('United_States_of_America', 'USA')\
    .replace('United_Kingdom', 'UK')\
    .sort_index()
top_five_countries = covid\
    .groupby('countriesAndTerritories').cases.sum()\
    .nlargest(5).index
covid[covid.countriesAndTerritories.isin(top_five_countries)]\
    .groupby('countriesAndTerritories').cases.idxmax()
covid\
    .groupby(['countriesAndTerritories', pd.Grouper(freq='1D')]).cases.sum()\
    .unstack(0).diff().rolling(7).mean().last('1W')[top_five_countries]
covid.reset_index()\
    .pivot(index='date', columns='countriesAndTerritories', values='cases')\
    .drop(columns='China')\
    .fillna(0)\
    .apply(lambda x: x[(x > 0)].idxmin())\
    .sort_values()\
    .rename(lambda x: x.replace('_', ' '))
covid\
    .pivot_table(columns='countriesAndTerritories', values='cases', aggfunc='sum')\
    .T\
    .transform('rank', method='max', pct=True)\
    .sort_values('cases', ascending=False)\
    .rename(lambda x: x.replace('_', ' '))
print()
