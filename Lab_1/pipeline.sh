#!/bin/bash

# Запуск скрипта создания данных
python data_creation.py

# Запуск скрипта предобработки данных
python model_preprocessing.py

# Запуск скрипта обучения модели
python model_preparation.py

# Запуск скрипта тестирования модели
python model_testing.py