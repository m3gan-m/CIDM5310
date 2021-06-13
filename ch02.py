print("Chapter 2 Exercises")
print("-------------------")
print()

import pandas as pd
df = pd.read_csv('data/parsed.csv')

print("1.", df[
    (df.parsed_place == 'Japan') & (df.magType == 'mb')
].mag.quantile(0.95))
print()

print("2. ",f"{df[df.parsed_place == 'Indonesia'].tsunami.value_counts(normalize=True).iloc[1,]:.2%}")
print()


print("3. ",df[df.parsed_place == 'Nevada'].describe())
print()

df['ring_of_fire'] = df.parsed_place.str.contains(r'|'.join([
    'Alaska', 'Antarctic', 'Bolivia', 'California', 'Canada',
    'Chile', 'Costa Rica', 'Ecuador', 'Fiji', 'Guatemala',
    'Indonesia', 'Japan', 'Kermadec Islands', '^Mexico',
    'New Zealand', 'Peru', 'Philippines', 'Russia',
    'Taiwan', 'Tonga', 'Washington' 
]))
#print("4. ",df.ring_of_fire)
print()

print("5. ",df.ring_of_fire.value_counts())
print()

print("6. ",df.loc[df.ring_of_fire, 'tsunami'].sum())