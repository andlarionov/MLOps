from catboost.datasets import titanic

# Загрузим датасет
data = titanic()

# Извлечем DataFrame из кортежа
df_titanic = data[0]

# Выберем нужные столбцы
df_titanic = df_titanic[['Pclass', 'Sex', 'Age']]

# Сохраняем тренировочный датасет
df_titanic.to_csv('datasets/df_titanic.csv', index=False)


