import numpy as np
import pandas as pd
import os
from sklearn.model_selection import train_test_split


# Задаем параметры для генерации данных
n_samples = 365  # Количество строк (дней в году)
n_features = 4   # Количество признаков


# Генерируем случайные данные для признаков
features = {
    f'feature_{i+1}': np.random.randn(n_samples) + np.random.normal(0, 0.5, n_samples) for i in range(n_features)
}

# Вставляем выбросы и шумы для каждого признака
outliers_indices = np.random.choice(n_samples, size=int(0.05 * n_samples), replace=False)
for feature in features.values():
    feature[outliers_indices] = np.random.uniform(-10, 10, len(outliers_indices))


# Генерируем случайные данные для температуры (целевой переменной)
features['Temperature'] = np.random.normal(20, 5, n_samples) + np.random.normal(0, 1, n_samples)


# Создаем DataFrame с признаками
data = pd.DataFrame(features)


# Разделяем признаки и целевую переменную
x, y = data.drop(columns = ['Temperature']), data['Temperature']

# Разбиваем на тренировочную и тестовую выборки
x_train, x_test, y_train, y_test = train_test_split(x, y,
                                                    test_size=0.2,
                                                    random_state=42)


# Создаем папки "train" и "test"
if not os.path.exists('train'):
    os.makedirs('train')
if not os.path.exists('test'):
    os.makedirs('test')


# Сохраняем данные в формате CSV
x_train.to_csv('Lab_1/train/x_train.csv', index=False)
y_train.to_csv('Lab_1/train/y_train.csv', index=False)
x_test.to_csv('Lab_1/test/x_test.csv', index=False)
y_test.to_csv('Lab_1/test/y_test.csv', index=False)