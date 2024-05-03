import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler


# функция разбиения на тренировочную и валидационную выборку
from sklearn.model_selection import train_test_split 

import warnings
warnings.filterwarnings('ignore')

DF = pd.read_csv('https://raw.githubusercontent.com/dayekb/mpti_ml/main/data/cars_moldova_clean.csv', delimiter = ',')

# Список числовых и категориальных данных
cat_columns = ['Make', 'Model', 'Style', 'Fuel_type', 'Transmission']
num_columns = ['Year', 'Distance', 'Engine_capacity(cm3)']

# Разбиваем на тренировочную и валидационную выборки
# Удаляем целевую переменную (цену) из признаков
X, y = DF.drop(columns = ['Price(euro)']), DF['Price(euro)']
features_names = list(DF.drop(columns = ["Price(euro)"]).columns)

# Преобразование категориальных признаков в в числовые
label_encoders = {}
for col in cat_columns:
    label_encoders[col] = LabelEncoder()
    X[col] = label_encoders[col].fit_transform(X[col])


# Создаем объект StandardScaler
scaler = StandardScaler()

# Применяем стандартизацию к числовым признакам
X[num_columns] = scaler.fit_transform(X[num_columns])


X_train, X_val, y_train, y_val = train_test_split(X, y,
                                                    test_size=0.3,
                                                    random_state=42)

X_train.to_csv('data_train.csv', index=False)
X_val.to_csv('x_valid.csv', index=False)
y_train.to_csv('y_train.csv', index=False)
y_val.to_csv('y_valid.csv', index=False)
