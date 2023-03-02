import pandas as pd

df = pd.read_csv('DS_cars.csv')

#doublons
duplicate = df[df.duplicated()]
if duplicate.empty:
    print('0 doublon')
else:
    print('Il y a des doublons')
    print(duplicate)

#valeurs nulles
null = df.isnull().sum()
if null.sum() == 0:
    print('0 valeur nulle')
else:
    print('Il y a des valeurs nulles')
    print(null)