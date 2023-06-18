import pandas as pd
dct = {'Numbers':[1, 2, 3, 4, 5],
       'Strings':['AB', 'BC', 'CD', 'DE', 'EF']}
df = pd.DataFrame(dct)
print(df)
Total = df['Numbers'].sum()
print("Numbers sum:", Total)
