FROM python:3.8

# Установка зависимостей
COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt


# Копирование файдов проекта
COPY . /app
WORKDIR /app


# Обучение модели
RUN python src/train_model.py


# Запуск Streamlit
CMD ["streamlit", "run", "src/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
