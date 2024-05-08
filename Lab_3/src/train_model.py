import os
import pickle
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


# Загружаем данные
df = load_iris()
X, y = df['data'], df['target']


# Формирование тренировочных и тестовых данных
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


# Обучение модели
model =  RandomForestClassifier(n_estimators = 150, random_state = 42)
model.fit(X_train, y_train)


# Сохранение модели
with open('src/iris_model.pkl', 'wb') as f:
    pickle.dump(model, f)

