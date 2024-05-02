import pickle
import pandas as pd
from sklearn.metrics import PredictionErrorDisplay
from sklearn.metrics import mean_squared_error


loaded_model = pickle.load(open('model_reg.pkl', 'rb'))


X_val = pd.read_csv('x_valid.csv')
y_val = pd.read_csv('y_valid.csv')


y_pred = loaded_model.predict(X_val)

# Вычисление среднеквадратичной ошибки
mse = mean_squared_error(y_val, y_pred)
print("Mean Squared Error:", mse)


PredictionErrorDisplay.from_predictions(
    y_val,
    loaded_model.predict(X_val),
    kind="actual_vs_predicted",
    scatter_kwargs={"alpha": 0.5},
);
