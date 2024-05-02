import lightgbm as lgb
from lightgbm import Dataset
import pickle
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import r2_score
from create_dataset import X, y
from create_dataset import cat_columns
from create_dataset import features_names


X_train = pd.read_csv('data_train.csv')
y_train = pd.read_csv('y_train.csv')
X_val = pd.read_csv('x_valid.csv')
y_val = pd.read_csv('y_valid.csv')

X_train = X_train.values
y_train = y_train.values
X_val = X_val.values
y_val = y_val.values

train_data = Dataset(
    X_train,
    y_train,
    categorical_feature=cat_columns,)

val_data = Dataset(
    X_val,
    y_val,
    categorical_feature=cat_columns,
)


# Создаем класс
model_reg = lgb.LGBMRegressor (random_state = 42,
                            objective= 'mean_squared_error',
                              categorical_feature =[0,1,3,6,7],
                             early_stopping_rounds=50,
                        n_estimators=500,)


# Обучаем модель и ищем лучшую итерацию
model_reg.fit(X_train, y_train,
          eval_set=[(X_train, y_train), (X_val, y_val)]);


print("Лучшая Итерация: {}".format(model_reg.best_iteration_))


# Обучаем модель и ищем лучшую итерацию
model_reg.fit(X_train,y_train,
          eval_set=[(X_train, y_train), (X_val, y_val)]);


print("Лучшая Итерация: {}".format(model_reg.best_iteration_))


# История обучения
results = model_reg.evals_result_


plt.figure(figsize=(10,7))
plt.plot(results["training"]["l2"], label="Потери на Тренировочных данных")
plt.plot(results["valid_1"]["l2"], label="Потери на Валидационных данных")
plt.xlabel("Количество Деревьев")
plt.ylabel("Потери")
plt.legend();


# Функция для визуализации значимости признаков
def feature_importance_plotter(model, features_names):
    """Отрисовка значимости признаков в виде горизонтальных столбчатых диаграмм.
    Параметры:
    ===========
    model: модель
    features_names: список имен признаков
    """
    feature_importance = model.feature_importances_

    sorted = np.argsort(feature_importance)

    ypos = np.arange(len(features_names))

    fig= plt.figure(figsize=(8,4))
    plt.barh(ypos, feature_importance[sorted])
    #plt.xlim([0,1])
    plt.ylabel('Параметры')
    plt.xlabel('Значимость')
    plt.yticks(ypos,features_names[sorted] );


# Визуализация значисоти признаков
feature_importance_plotter(model_reg, np.array(features_names))


# Функция для оценки метрик
def calculate_metric(model_pipe, X, y, metric = r2_score):
    """Расчет метрики.
    Параметры:
    ===========
    model_pipe: модель или pipeline
    X: признаки
    y: истинные значения
    metric: метрика (r2 - по умолчанию)
    """
    y_model = model_pipe.predict(X)
    return metric(y, y_model)


# Оценка метрик
print(f"r2 на тренировочной выборке: {calculate_metric(model_reg, X_train, y_train):.4f}")
print(f"r2 на валидационной выборке: {calculate_metric(model_reg, X_val, y_val):.4f}")

print(f"mse на тренировочной выборке: {calculate_metric(model_reg, X_train, y_train, mse):.4f}")
print(f"mse на валидационной выборке: {calculate_metric(model_reg, X_val, y_val, mse):.4f}")


# Сохраняем модель
pickle.dump(model_reg, open('model_reg.pkl', 'wb'))
