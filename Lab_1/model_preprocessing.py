from sklearn.preprocessing import StandardScaler
import pandas as pd


# Загрузка данных для предобработки
x_train = pd.read_csv('train/x_train.csv')
x_test = pd.read_csv('test/x_test.csv')


# Предобработка данных
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)