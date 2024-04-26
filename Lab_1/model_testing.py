import pandas as pd
from sklearn.metrics import mean_squared_error as mse
from model_preparation import model
from model_preprocessing import x_test_scaled
from data_creation import y_test


y_pred = model.predict(x_test_scaled)


# Вычисляем среднеквадратичную ошибку
mse_score = mse(y_test, y_pred)


print("MSE:", mse_score)