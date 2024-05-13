import pandas as pd

df_titanic = pd.read_csv('datasets/df_titanic.csv', sep=',')

import pandas as pd

# Получаем средний возраст
mean_age = round(df_titanic['Age'].mean(), 1)

# Заменяем пропущенные значения средним возрастом
df_titanic['Age'].fillna(mean_age, inplace=True)

df_titanic.to_csv('datasets/df_titanic.csv', index=False)
