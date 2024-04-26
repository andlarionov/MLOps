from sklearn.linear_model import LinearRegression
from model_preprocessing import x_train_scaled
import pandas as pd


# Загрузка целевого признака для тренировочных данных
y_train = pd.read_csv('train/y_train.csv')  


# Создание и обучение модели
model = LinearRegression()
model.fit(x_train_scaled, y_train)